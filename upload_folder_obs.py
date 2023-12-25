import os
from obs import ObsClient

def upload_folder_to_obs(local_folder_path, bucket_name, obs_folder_path, obs_client):
    for root, dirs, files in os.walk(local_folder_path):
        for file_name in files:
            local_file_path = os.path.join(root, file_name)
            relative_path = os.path.relpath(local_file_path, local_folder_path)
            obs_file_path = os.path.join(obs_folder_path, relative_path) if obs_folder_path else relative_path
            print(f"Uploading {local_file_path} to OBS path {obs_file_path}")
            obs_client.putFile(bucket_name, obs_file_path, local_file_path)

def main():
    ak = 'EY46QRM1OA4GI10PJDSU'
    sk = '6x5zWLdUtP6qNFCrK7A7177Er3v8ehAHsw8tIHnJ'
    obs_endpoint = 'obs.cn-north-4.myhuaweicloud.com'
    bucket_name = 'aitextvideopub'
    local_folder_path = '/mnt/nvm2/aitexttovideo/漫画推文BGM'
    obs_folder_path = 'music/' # OBS中的目标文件夹路径

    obs_client = ObsClient(access_key_id=ak, secret_access_key=sk, server=obs_endpoint)
    upload_folder_to_obs(local_folder_path, bucket_name, obs_folder_path, obs_client)

if __name__ == "__main__":
    main()

