from utils.utils import *

vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
print(vdud.title)
print(vdud.num_videos)
print(vdud.channel_url)
# vdud.channel_id= 'Новое название'
print(Channel.get_service)
vdud.save_to_json('vdud.json')

