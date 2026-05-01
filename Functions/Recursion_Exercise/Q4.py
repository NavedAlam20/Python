def toh(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    toh(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    toh(n-1, auxiliary, source, destination)

n = int(input())
toh(n, 'A', 'B', 'C')