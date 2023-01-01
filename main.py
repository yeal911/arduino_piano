import socket
import pygame

def main():
  # 音名列表
  note_names = ['C3', 'Db3', 'D3', 'Eb3', 'E3', 'F3', 'Gb3', 'G3', 'Ab3', 'A3', 'Bb3', 'B3',
                'C4', 'Db4', 'D4', 'Eb4', 'E4', 'F4', 'Gb4', 'G4', 'Ab4', 'A4', 'Bb4', 'B4',
                'C5', 'Db5', 'D5', 'Eb5', 'E5', 'F5', 'Gb5', 'G5', 'Ab5', 'A5', 'Bb5', 'B5']
  # 创建空的字典
  mp3_files = {}
  # 遍历音名列表
  for i, note_name in enumerate(note_names):
    # 将音名映射到对应的文件名
    file_name = "/home/tao/Arduino/piano-mp3/" + f'{note_name}.mp3'
    # 将文件名存储到字典中
    mp3_files[i] = file_name
  # 绑定地址和端口
  address = ('', 8888)
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.bind(address)
  # 监听并接收消息
  while True:
    data, addr = s.recvfrom(1024)
    message = data.decode('utf-8')
    print('Received from %s: %s' % (addr, message))
    # 发送响应
    if message == 'PIANO':
      s.sendto(b'yes, i am', addr)
    else:
      # 加载音频文件
      pygame.mixer.init()
      sound = pygame.mixer.Sound(mp3_files[int(message)])
      # 播放音频
      sound.play()

if __name__ == '__main__':
  main()