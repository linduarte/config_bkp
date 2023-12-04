import shutil

# Define the paths of the files to be backed up
fig_us_path = "C:/Users/clldu/.gitconfig"
fig_sy_path = "C:/Program Files/Git/etc/gitconfig"

# Define the backup destinations
backup_dir1 = "C:/Users/clldu/OneDrive/Documentos/myconfigs/back_us/"
backup_dir2 = "C:/Users/clldu/OneDrive/Documentos/myconfigs/back_sy/"

# Create backups
shutil.copy(fig_us_path, backup_dir1)
shutil.copy(fig_sy_path, backup_dir2)

print("Backup completed successfully!")
