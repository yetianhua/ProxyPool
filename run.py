from proxypool.scheduler import Scheduler
import argparse

# argsparse是python的命令行解析的标准模块，内置于python，不需要安装。
parser = argparse.ArgumentParser(description='ProxyPool')
# 添加参数 type是要传入的参数的数据类型  help是该参数的提示信息
# 使用可选参数，这个有点像关键词传参，但是需要在关键词前面加--
parser.add_argument('--processor', type=str, help='processor to run')
args = parser.parse_args()

if __name__ == '__main__':
    # if processor set, just run it
    if args.processor:
        # getattr方法获取对象方法
        # 执行run_{args.processor}方法
        # f'run_{args.processor}'是f-string语法，用来其開頭是f，花括號「 { } 」裡面放入參數名稱，字串則使用雙引號（ “ ” ）標註
        getattr(Scheduler(), f'run_{args.processor}')()
    else:
        Scheduler().run()
