# coding: UTF-8

from Chinese_poem_generator.config import *
from Chinese_poem_generator import data
from Chinese_poem_generator import model

def defineArgs():
    """define args"""
    parser = argparse.ArgumentParser(description = "Chinese_poem_generator.")
    parser.add_argument("-k", help = "select mode by 'train' or test or head")
    parser.add_argument("-m", "--mode", help = "select mode by 'train' or test or head",
                        choices = ["train", "test", "head"], default = "test")
	
    return parser.parse_args()


if __name__ == "__main__":
    args = defineArgs()
    trainData = data.POEMS(trainPoems)
    MCPangHu = model.MODEL(trainData)
    if args.mode == "train":
        MCPangHu.train()
    else:
        if args.mode == "test":
            poems = MCPangHu.test()
        else:
            characters = args.k
            poems = MCPangHu.testHead(characters)
