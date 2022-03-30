class F:
    def __init__(self) -> None:
        pass


class G(F):
    def __init__(self) -> None:
        pass


class H(G):
    def __init__(self) -> None:
        pass


if __name__ == '__main__':
    f = F()
    g = G()
    h = H()

# isinstance is the same
# type is different

# Why should abstract classes never be instantiated?
