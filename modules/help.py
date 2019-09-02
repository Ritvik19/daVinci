def help():
    with open('README.md') as f:
        commands = list(map(lambda x : x.strip(), f.readlines()))
    return '\n'.join(commands[7:]).replace('`', '')

if __name__ == '__main__':
    print(help())
