# pip -q install dominate
# pip -q install opencv-python

chmod +rx ./generation/scripts/encode_texture_features_demo.sh
chmod +rx ./separate_vae/scripts/encode_shape_features_demo.sh


cd ./preprocess
bash run_prepare_data.sh
bash encode_shape_texture_features.sh
cd ..


# ##################################
############# INFERENCE

cd  ./classification/data_dict/shape_and_feature
bash scripts/edit_and_visualize_demo.sh $1 shape_and_texture True 2 100 0.25


#######################################
