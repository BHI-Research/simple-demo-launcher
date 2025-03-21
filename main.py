import torch


def main_function():
    x = torch.rand(5, 3)
    print(x)
    if torch.cuda.is_available():
        print("using GPU")
    else:
        print("using CPU")


if __name__ == "__main__":
    main_function()
