def is_feasible(x):
    """
    例として、
    - x の値が 100 以下なら条件を満たす
    という単純な判定にしています。
    実際には問題や目的に合わせて中身を書き換えてください。
    """
    return x <= 100

def bsearch(low, high):
    """
    low ~ high の整数範囲で二分探索を行い、
    is_feasible(x) が True となる最大の x を返す。
    条件を満たす x が存在しない場合は None を返す。
    """
    # 条件を満たす値が見つからなかったとき用のフラグ(または値)
    ans = None

    while low <= high:
        mid = (low + high) // 2
        
        if is_feasible(mid):
            # mid が条件を満たすなら、さらに大きい値を探す
            ans = mid        # 条件を満たす候補
            low = mid + 1    # 右半分を探索
        else:
            # mid が条件を満たさないなら、左半分を探索
            high = mid - 1
    
    return ans

if __name__ == "__main__":
    # 例えば、0 ~ 1000 の範囲で
    # is_feasible(x) が True になる最大の x を探す
    result = bsearch(0, 1000)
    if result is not None:
        print(f"条件を満たす最大の値は: {result}")
    else:
        print("条件を満たす値は存在しません。")