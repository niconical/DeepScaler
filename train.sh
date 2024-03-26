# AdapGL+ASTGCN
python ./main_cpu.py \
    --model_config_path config/train_dataset_speed.yaml \
    --train_config_path config/train_config.yaml \
    --model_name AdapGLA \
    --num_epoch 4 \
    --num_iter 20 \
    --model_save_path model_states/AdapGLA_boutique/AdapGLA_boutique.pkl \
    --max_graph_num 1

# # AdapGL+DCRNN 
# python ./main_cpu.py \
#     --model_config_path config/train_dataset_speed.yaml \
#     --train_config_path config/train_config.yaml \
#     --model_name AdapGLD \
#     --num_epoch 5 \
#     --num_iter 20 \
#     --model_save_path model_states/AdapGLD_boutique/AdapGLD_boutique.pkl \
#     --max_graph_num 1

# # AdapGL+TGCN
# python ./main_cpu.py \
#     --model_config_path config/train_dataset_speed.yaml \
#     --train_config_path config/train_config.yaml \
#     --model_name AdapGLT \
#     --num_epoch 5 \
#     --num_iter 20 \
#     --model_save_path model_states/AdapGLT_boutique/AdapGLT_boutique.pkl \
#     --max_graph_num 1
