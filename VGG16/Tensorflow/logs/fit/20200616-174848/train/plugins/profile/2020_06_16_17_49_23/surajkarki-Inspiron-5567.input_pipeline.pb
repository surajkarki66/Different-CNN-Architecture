	d=�J��@d=�J��@!d=�J��@	��G�?��G�?!��G�?"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$d=�J��@�1�%d�?Ayy:W���@Y�sCSv�?*	�I+�N@2j
3Iterator::Model::ParallelMap::Zip[1]::ForeverRepeat8H��-�?!ل���@@)�P�y�?1R:�m=@:Preprocessing2S
Iterator::Model::ParallelMapR,���?!�0�g`2@)R,���?1�0�g`2@:Preprocessing2F
Iterator::Model*V���?!c���xA@)�cϞ˄?1/;��0@:Preprocessing2t
=Iterator::Model::ParallelMap::Zip[0]::FlatMap[0]::Concatenate������?!��Һ�3@)�_!se�?1�L��?*@:Preprocessing2X
!Iterator::Model::ParallelMap::Zip�3�l�?!ή�8�CP@)j�����u?1��:ihr!@:Preprocessing2�
MIterator::Model::ParallelMap::Zip[0]::FlatMap[0]::Concatenate[0]::TensorSliceOI�Vq?!ӥŦk�@)OI�Vq?1ӥŦk�@:Preprocessing2d
-Iterator::Model::ParallelMap::Zip[0]::FlatMapWzm6Vb�?!!Q&�-38@)[�*�MFe?1��D��@:Preprocessing2v
?Iterator::Model::ParallelMap::Zip[1]::ForeverRepeat::FromTensor�t?� ?[?![G s�@)�t?� ?[?1[G s�@:Preprocessing:�
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
�Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
�Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
�Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
�Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)�
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis�
device�Your program is NOT input-bound because only 0.0% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*no#You may skip the rest of this page.B�
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown�
	�1�%d�?�1�%d�?!�1�%d�?      ��!       "      ��!       *      ��!       2	yy:W���@yy:W���@!yy:W���@:      ��!       B      ��!       J	�sCSv�?�sCSv�?!�sCSv�?R      ��!       Z	�sCSv�?�sCSv�?!�sCSv�?JCPU_ONLY