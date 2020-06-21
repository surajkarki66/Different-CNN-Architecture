import tensorflow as tf


class Conv_Bn(tf.keras.layers.Layer):
    """ Basic conv2d -> batch_normalization -> ReLU layer """

    def __init__(self, filters, kernel_size, strides, padding):
        super(Conv_Bn, self).__init__()
        self.conv = tf.keras.layers.Conv2D(filters=filters,
                                           kernel_size=kernel_size,
                                           strides=strides,
                                           padding=padding)
        self.bn = tf.keras.layers.BatchNormalization()
        self.relu = tf.keras.layers.ReLU()

    def call(self, inputs, training=None, **kwargs):
        output = self.conv(inputs)
        output = self.bn(output, training=training)
        output = self.relu(output)

        return output


class Preprocess(tf.keras.layers.Layer):
    def __init__(self):
        super(Preprocess, self).__init__()
        self.conv1 = Conv_Bn(filters=32,
                             kernel_size=(3, 3),
                             strides=2,
                             padding="same")
        self.conv2 = Conv_Bn(filters=32,
                             kernel_size=(3, 3),
                             strides=1,
                             padding="same")
        self.conv3 = Conv_Bn(filters=64,
                             kernel_size=(3, 3),
                             strides=1,
                             padding="same")

        self.maxpool1 = tf.keras.layers.MaxPool2D(pool_size=(3, 3),
                                                  strides=2,
                                                  padding="same")
        self.conv4 = Conv_Bn(filters=80,
                             kernel_size=(1, 1),
                             strides=1,
                             padding="same")
        self.conv5 = Conv_Bn(filters=192,
                             kernel_size=(3, 3),
                             strides=1,
                             padding="same")
        self.maxpool2 = tf.keras.layers.MaxPool2D(pool_size=(3, 3),
                                                  strides=2,
                                                  padding="same")

    def call(self, inputs, training=None, **kwargs):
        x = self.conv1(inputs, training=training)
        x = self.conv2(x, training=training)
        x = self.conv3(x, training=training)
        x = self.maxpool1(x)
        x = self.conv4(x, training=training)
        x = self.conv5(x, training=training)
        x = self.maxpool2(x)

        return x


class InceptionAuxOutput(tf.keras.layers.Layer):
    """ Auxillary output layer """

    def __init__(self, num_classes):
        super(InceptionAuxOutput, self).__init__()
        self.avg_pool = tf.keras.layers.AvgPool2D(pool_size=(5, 5),
                                                  strides=3,
                                                  padding="same")
        self.conv1 = Conv_Bn(filters=128,
                             kernel_size=(1, 1),
                             strides=1,
                             padding="same")
        self.conv2 = Conv_Bn(filters=768,
                             kernel_size=(5, 5),
                             strides=1,
                             padding="same")
        self.global_avg_pool = tf.keras.layers.GlobalAveragePooling2D()
        self.flat = tf.keras.layers.Flatten()
        self.fc = tf.keras.layers.Dense(
            units=num_classes, activation=tf.keras.activations.linear)

    def call(self, inputs, training=None, **kwargs):
        output = self.avg_pool(inputs)
        output = self.conv1(output, training=training)
        output = self.conv2(output, training=training)
        output = self.global_avg_pool(output)
        output = self.flat(output)
        output = self.fc(output)

        return output


class InceptionModule_1(tf.keras.layers.Layer):
    def __init__(self, filter_num):
        super(InceptionModule_1, self).__init__()
        # branch 0
        self.conv_b0_1 = Conv_Bn(filters=64,
                                 kernel_size=(1, 1),
                                 strides=1,
                                 padding="same")

        # branch 1
        self.conv_b1_1 = Conv_Bn(filters=48,
                                 kernel_size=(1, 1),
                                 strides=1,
                                 padding="same")

        self.conv_b1_2 = Conv_Bn(filters=64,
                                 kernel_size=(5, 5),
                                 strides=1,
                                 padding="same")

        # branch 2
        self.conv_b2_1 = Conv_Bn(filters=64,
                                 kernel_size=(1, 1),
                                 strides=1,
                                 padding="same")

        self.conv_b2_2 = Conv_Bn(filters=96,
                                 kernel_size=(3, 3),
                                 strides=1,
                                 padding="same")
        self.conv_b2_3 = Conv_Bn(filters=96,
                                 kernel_size=(3, 3),
                                 strides=1,
                                 padding="same")

        # branch 3
        self.avgpool_b3_1 = tf.keras.layers.AvgPool2D(pool_size=(3, 3),
                                                      strides=1,
                                                      padding="same")
        self.conv_b3_2 = Conv_Bn(filters=filter_num,
                                 kernel_size=(1, 1),
                                 strides=1,
                                 padding="same")

    def call(self, inputs, training=None, **kwargs):

        b0 = self.conv_b0_1(inputs, training=training)

        b1 = self.conv_b1_1(inputs, training=training)
        b1 = self.conv_b1_2(b1, training=training)

        b2 = self.conv_b2_1(inputs, training=training)
        b2 = self.conv_b2_2(b2, training=training)
        b2 = self.conv_b2_3(b2, training=training)

        b3 = self.avgpool_b3_1(inputs)
        b3 = self.conv_b3_2(b3, training=training)

        output = tf.keras.layers.concatenate([b0, b1, b2, b3], axis=-1)
        return output


class InceptionModule_2(tf.keras.layers.Layer):
    def __init__(self):
        super(InceptionModule_2, self).__init__()
        # branch 0
        self.conv_b0_1 = Conv_Bn(filters=384,
                                 kernel_size=(3, 3),
                                 strides=2,
                                 padding="valid")

        # branch 1
        self.conv_b1_1 = Conv_Bn(filters=64,
                                 kernel_size=(1, 1),
                                 strides=1,
                                 padding="same")
        self.conv_b1_2 = Conv_Bn(filters=96,
                                 kernel_size=(3, 3),
                                 strides=1,
                                 padding="same")
        self.conv_b1_3 = Conv_Bn(filters=96,
                                 kernel_size=(3, 3),
                                 strides=2,
                                 padding="valid")

        # branch 2
        self.maxpool_b2_1 = tf.keras.layers.MaxPool2D(pool_size=(3, 3),
                                                      strides=2,
                                                      padding="valid")

    def call(self, inputs, training=None, **kwargs):
        b0 = self.conv_b0_1(inputs, training=training)

        b1 = self.conv_b1_1(inputs, training=training)
        b1 = self.conv_b1_2(b1, training=training)
        b1 = self.conv_b1_3(b1, training=training)

        b2 = self.maxpool_b2_1(inputs)

        output = tf.keras.layers.concatenate([b0, b1, b2], axis=-1)
        return output


class InceptionModule_3(tf.keras.layers.Layer):
    def __init__(self, filter_num):
        super(InceptionModule_3, self).__init__()
        # branch 0
        self.conv_b0_1 = Conv_Bn(filters=192,
                                 kernel_size=(1, 1),
                                 strides=1,
                                 padding="same")

        # branch 1
        self.conv_b1_1 = Conv_Bn(filters=filter_num,
                                 kernel_size=(1, 1),
                                 strides=1,
                                 padding="same")
        self.conv_b1_2 = Conv_Bn(filters=filter_num,
                                 kernel_size=(1, 7),
                                 strides=1,
                                 padding="same")
        self.conv_b1_3 = Conv_Bn(filters=192,
                                 kernel_size=(7, 1),
                                 strides=1,
                                 padding="same")

        # branch 2
        self.conv_b2_1 = Conv_Bn(filters=filter_num,
                                 kernel_size=(1, 1),
                                 strides=1,
                                 padding="same")
        self.conv_b2_2 = Conv_Bn(filters=filter_num,
                                 kernel_size=(7, 1),
                                 strides=1,
                                 padding="same")
        self.conv_b2_3 = Conv_Bn(filters=filter_num,
                                 kernel_size=(1, 7),
                                 strides=1,
                                 padding="same")
        self.conv_b2_4 = Conv_Bn(filters=filter_num,
                                 kernel_size=(7, 1),
                                 strides=1,
                                 padding="same")
        self.conv_b2_5 = Conv_Bn(filters=192,
                                 kernel_size=(1, 7),
                                 strides=1,
                                 padding="same")

        # branch 3
        self.avgpool_b3_1 = tf.keras.layers.MaxPool2D(pool_size=(3, 3),
                                                      strides=1,
                                                      padding="same")
        self.conv_b3_2 = Conv_Bn(filters=192,
                                 kernel_size=(1, 1),
                                 strides=1,
                                 padding="same")

    def call(self, inputs, training=None, **kwargs):
        b0 = self.conv_b0_1(inputs, training=training)

        b1 = self.conv_b1_1(inputs, training=training)
        b1 = self.conv_b1_2(b1, training=training)
        b1 = self.conv_b1_3(b1, training=training)

        b2 = self.conv_b2_1(inputs, training=training)
        b2 = self.conv_b2_2(b2, training=training)
        b2 = self.conv_b2_3(b2, training=training)
        b2 = self.conv_b2_4(b2, training=training)
        b2 = self.conv_b2_5(b2, training=training)

        b3 = self.avgpool_b3_1(inputs)
        b3 = self.conv_b3_2(b3, training=training)

        output = tf.keras.layers.concatenate([b0, b1, b2, b3], axis=-1)
        return output


class InceptionModule_4(tf.keras.layers.Layer):
    def __init__(self):
        super(InceptionModule_4, self).__init__()
        # branch 0
        self.conv_b0_1 = Conv_Bn(filters=192,
                                 kernel_size=(1, 1),
                                 strides=1,
                                 padding="same")
        self.conv_b0_2 = Conv_Bn(filters=320,
                                 kernel_size=(3, 3),
                                 strides=2,
                                 padding="valid")

        # branch 1
        self.conv_b1_1 = Conv_Bn(filters=192,
                                 kernel_size=(1, 1),
                                 strides=1,
                                 padding="same")

        self.conv_b1_2 = Conv_Bn(filters=192,
                                 kernel_size=(1, 7),
                                 strides=1,
                                 padding="same")

        self.conv_b1_3 = Conv_Bn(filters=192,
                                 kernel_size=(7, 1),
                                 strides=1,
                                 padding="same")

        self.conv_b1_4 = Conv_Bn(filters=192,
                                 kernel_size=(3, 3),
                                 strides=2,
                                 padding="valid")

        # branch 2
        self.maxpool_b2_1 = tf.keras.layers.MaxPool2D(pool_size=(3, 3),
                                                      strides=2,
                                                      padding="valid")

    def call(self, inputs, training=None, **kwargs):
        b0 = self.conv_b0_1(inputs, training=training)
        b0 = self.conv_b0_2(b0, training=training)

        b1 = self.conv_b1_1(inputs, training=training)
        b1 = self.conv_b1_2(b1, training=training)
        b1 = self.conv_b1_3(b1, training=training)
        b1 = self.conv_b1_4(b1, training=training)

        b2 = self.maxpool_b2_1(inputs)

        output = tf.keras.layers.concatenate([b0, b1, b2], axis=-1)
        return output


class InceptionModule_5(tf.keras.layers.Layer):
    def __init__(self):
        super(InceptionModule_5, self).__init__()
        self.conv1 = Conv_Bn(filters=320,
                             kernel_size=(1, 1),
                             strides=1,
                             padding="same")
        self.conv2 = Conv_Bn(filters=384,
                             kernel_size=(1, 1),
                             strides=1,
                             padding="same")
        self.conv3 = Conv_Bn(filters=448,
                             kernel_size=(1, 1),
                             strides=1,
                             padding="same")
        self.conv4 = Conv_Bn(filters=384,
                             kernel_size=(1, 3),
                             strides=1,
                             padding="same")
        self.conv5 = Conv_Bn(filters=384,
                             kernel_size=(3, 1),
                             strides=1,
                             padding="same")
        self.conv6 = Conv_Bn(filters=384,
                             kernel_size=(3, 3),
                             strides=1,
                             padding="same")
        self.conv7 = Conv_Bn(filters=192,
                             kernel_size=(1, 1),
                             strides=1,
                             padding="same")
        self.avgpool = tf.keras.layers.AvgPool2D(pool_size=(3, 3),
                                                 strides=1,
                                                 padding="same")

    def call(self, inputs, training=None, **kwargs):
        b0 = self.conv1(inputs, training=training)

        b1 = self.conv2(inputs, training=training)
        b1_part_a = self.conv4(b1, training=training)
        b1_part_b = self.conv5(b1, training=training)
        b1 = tf.keras.layers.concatenate([b1_part_a, b1_part_b], axis=-1)

        b2 = self.conv3(inputs, training=training)
        b2 = self.conv6(b2, training=training)
        b2_part_a = self.conv4(b2, training=training)
        b2_part_b = self.conv5(b2, training=training)
        b2 = tf.keras.layers.concatenate([b2_part_a, b2_part_b], axis=-1)
        b3 = self.avgpool(inputs)
        b3 = self.conv7(b3, training=training)

        output = tf.keras.layers.concatenate([b0, b1, b2, b3], axis=-1)
        return output
