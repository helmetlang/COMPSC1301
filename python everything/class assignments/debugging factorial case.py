def facto(n, indent=""):
    print(indent, f"Computing {n} factorial...")
    if n<= 1:
        return 1
    else:
        return n * facto(n-1, indent+"  ")