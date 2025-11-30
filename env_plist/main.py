import os
import plistlib
from shutil import copyfile

current_path = os.path.dirname(os.path.abspath(__file__))

# 0. region
regions = [
    "HK",
    "SG",
    "UK",
    "US",
]

# 1.all the envs
envs = [
    "SITMA",
    "UATMA",
    "Debug",
    "Dev",
    "Prod",
]

ignore_envs = [
    "Debug",
    "Dev",
    "Prod",
]

# 2. get the env and region
print("Our region support as below:")
print("======")
for el in regions: print(el)
print("======")
region = input("please input the region you want: ")
print('\r\n')
print("Our markets env as below:")
print("======")
for el in envs: print(el)
print("======")
env = input("please input the env you want: ")

# if  in ignore_envs just copy the file as MobileConfig.plist
if env in ignore_envs:
    copyfile(f"{current_path}/{region}/envs/MobileConfig_{env}.plist", f"{current_path}/{region}/MobileConfig.plist")
    print(f"{current_path}/{region}/envs/MobileConfig_{env}.plist", f"{current_path}/{region}/MobileConfig.plist")
    exit(1)

# 3. get the envs.plist
with open('envs.plist') as f: envs_plist = plistlib.loads(bytes(f.read().encode("utf8")))
print(f'envs.plist -> {env}: {envs_plist[region][env]}')

# 4. get the correct plist and modify it
with open(f'{current_path}/{region}/envs/MobileConfig_Develop.plist') as f: region_plist = plistlib.loads(
    bytes(f.read().encode("utf8")))
print(f'region.plist -> {region}: {region_plist}')

region_plist.update(envs_plist[region][env])
print(f"current region_plist -> : {region_plist}")

with open(f'{current_path}/{region}/MobileConfig.plist', 'wb') as f:
    plistlib.dump(region_plist, f)
