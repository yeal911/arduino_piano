import socket
import pygame


def main():
    # 音名列表
    global sound
    low_note_names = ['', '', '', '', '', '', '', '', '', 'A0', 'Bb0', 'B0',
                      'C1', 'Db1', 'D1', 'Eb1', 'E1', 'F1', 'Gb1', 'G1', 'Ab1', 'A1', 'Bb1', 'B1',
                      'C2', 'Db2', 'D2', 'Eb2', 'E2', 'F2', 'Gb2', 'G2', 'Ab2', 'A2', 'Bb2', 'B2']

    mid_note_names = ['C3', 'Db3', 'D3', 'Eb3', 'E3', 'F3', 'Gb3', 'G3', 'Ab3', 'A3', 'Bb3', 'B3',
                      'C4', 'Db4', 'D4', 'Eb4', 'E4', 'F4', 'Gb4', 'G4', 'Ab4', 'A4', 'Bb4', 'B4',
                      'C5', 'Db5', 'D5', 'Eb5', 'E5', 'F5', 'Gb5', 'G5', 'Ab5', 'A5', 'Bb5', 'B5']

    hig_note_names = ['C6', 'Db6', 'D6', 'Eb6', 'E6', 'F6', 'Gb6', 'G6', 'Ab6', 'A6', 'Bb6', 'B6',
                      'C7', 'Db7', 'D7', 'Eb7', 'E7', 'F7', 'Gb7', 'G7', 'Ab7', 'A7', 'Bb7', 'B7',
                      'C8', 'Db8', '', '', '', '', '', '', '', '', '', '']
    # 创建空的字典
    low_mp3_files = {}
    mid_mp3_files = {}
    hig_mp3_files = {}
    # 遍历音名列表
    for i in range(0, len(mid_note_names)):
        # /home/tao/Arduino/piano-mp3/
        # 将音名映射到对应的文件名
        low_file_name = "D:\\Development\\piano-mp3-master\\piano-mp3\\" + f'{low_note_names[i]}.mp3'
        mid_file_name = "D:\\Development\\piano-mp3-master\\piano-mp3\\" + f'{mid_note_names[i]}.mp3'
        hig_file_name = "D:\\Development\\piano-mp3-master\\piano-mp3\\" + f'{hig_note_names[i]}.mp3'
        # 将文件名存储到字典中
        low_mp3_files[i] = low_file_name
        mid_mp3_files[i] = mid_file_name
        hig_mp3_files[i] = hig_file_name

    # 绑定地址和端口
    address = ('', 8888)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(address)
    # 初始化音频
    pygame.mixer.init()
    # 监听并接收消息
    while True:
        data, addr = s.recvfrom(1024)
        message = data.decode('utf-8')
        print('Received from %s: %s' % (addr, message))
        # 发送响应
        if message == 'PIANO':
            s.sendto(b'YES', addr)
        else:
            if message[0:3] == "LOW":
                if low_note_names[int(message[3:])] != "":
                    sound = pygame.mixer.Sound(low_mp3_files[int(message[3:])])
            elif message[0:3] == "MID":
                sound = pygame.mixer.Sound(mid_mp3_files[int(message[3:])])
            elif message[0:3] == "HIG":
                if hig_note_names[int(message[3:])] != "":
                    sound = pygame.mixer.Sound(hig_mp3_files[int(message[3:])])
            else:
                print("invalid message.")
          # 播放音频
        sound.play()


if __name__ == '__main__':
    main()
