# 挂载
# 查看
df -h [dir]
fdisk -l

## WSL /home 挂载 F:\
sudo umount /mnt/f
sudo mount -t drvfs 'F:\' /home
