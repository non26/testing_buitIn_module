def test_recursive(count):
    cnt = count
    if cnt == 10:
        print(f"running out from {cnt}")
    else:
        cnt += 1
        test_recursive(cnt)
        cnt -= 1
        print(cnt)
test_recursive(0)