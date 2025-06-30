#数据集生成

##1下载公开数据集IM-TQA

##2运行生成数据集代码

```python data_to_imtsrtqa.py```

#模型训练

##合并实验-Text2Cell

训练

python train.py --dataroot ./datasets/icdar13table --gpu_ids 1 --model res2tim --dataset_mode cell_rel --lr 0.0005 --pair_batch 10000 --niter 5 --niter_decay 95 --use_mask --name res2tim_icdar13table

测试

python test.py --dataroot ./datasets/icdar13table --gpu_ids 1 --model res2tim --dataset_mode cell_rel --pair_batch 10000 --use_mask --name res2tim_icdar13table --epoch best

##关系实验-相邻与关系实验-同行列

在cmdd数据集训练

python train.py --dataroot ./datasets/cmdd --gpu_ids 1 --model res2tim --dataset_mode cell_rel --lr 0.0005 --pair_batch 10000 --niter 5 --niter_decay 95 --use_mask --name res2tim_cmdd

在cmdd数据集测试

python test.py --dataroot ./datasets/cmdd --gpu_ids 1 --model res2tim --dataset_mode cell_rel --pair_batch 10000 --use_mask --name res2tim_cmdd --epoch best

复制最佳到icdar13训练任务

mkdir ./checkpoints/icdar13table

cp ./checkpoints/cmdd/best_net_Res2Tim.pth ./checkpoints/icdar13table/best_net_Res2Tim.pth

在icadr13数据集训练

python train.py --dataroot ./datasets/icdar13table --gpu_ids 1 --model res2tim --dataset_mode cell_rel --lr 0.0005 --pair_batch 10000 --niter 5 --niter_decay 95 --use_mask --name res2tim_icdar13table --continue_train --epoch prt

在icadr13数据集测试

python test.py --dataroot ./datasets/icdar13table --gpu_ids 1 --model res2tim --dataset_mode cell_rel --pair_batch 10000 --use_mask --name res2tim_icdar13table --epoch best

在imtqa数据集训练

python train.py --dataroot ./datasets/icdar13table --gpu_ids 1 --model res2tim --dataset_mode cell_rel --lr 0.0005 --pair_batch 10000 --niter 5 --niter_decay 95 --use_mask --name res2tim_icdar13table

在imtqa数据集测试

python test.py --dataroot ./datasets/icdar13table --gpu_ids 1 --model res2tim --dataset_mode cell_rel --pair_batch 10000 --use_mask --name res2tim_icdar13table --epoch best

表格信息准确率指标tia计算

tia.py
