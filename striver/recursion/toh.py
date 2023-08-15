def toh(n, source, auxiliary, destination, ans):
    if n == 0:
        return
    toh(n-1, source, destination, auxiliary, ans)
    ans.append([source, destination])
    toh(n-1, auxiliary, source, destination, ans)


def towerOfHanoi(n):
    ans = []
    toh(n, 1, 2, 3, ans)
    return ans


# another code

def move(disks, source=1, auxiliary=2, target=3):

    if disks > 0:

        # move `n-1` discs from source to auxiliary using the target
        # as an intermediate pole
        move(disks - 1, source, target, auxiliary)

        # move one disc from source to target
        print(f'Move disk {disks} from {source} —> {target}')

        # move `n-1` discs from auxiliary to target using the source
        # as an intermediate pole
        move(disks - 1, auxiliary, source, target)


# Tower of Hanoi Problem
if __name__ == '__main__':

    n = 3
    move(n)
