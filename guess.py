"""1~100 사이의 숫자를 맞히는 간단한 게임."""

import random

LOW, HIGH = 1, 100


def play():
    answer = random.randint(LOW, HIGH)
    attempts = 0
    print(f"{LOW}부터 {HIGH} 사이의 숫자를 맞혀 보세요!")

    while True:
        try:
            text = input("숫자 입력: ")
        except EOFError:
            print(f"\n게임을 종료합니다. (정답: {answer})")
            return

        try:
            guess = int(text)
        except ValueError:
            print("숫자를 입력해 주세요.")
            continue

        if not LOW <= guess <= HIGH:
            print(f"{LOW}부터 {HIGH} 사이의 숫자를 입력해 주세요.")
            continue

        attempts += 1
        if guess < answer:
            print(f"더 큽니다! (시도 {attempts}회)")
        elif guess > answer:
            print(f"더 작습니다! (시도 {attempts}회)")
        else:
            print(f"정답입니다! {attempts}번 만에 맞혔어요.")
            return


if __name__ == "__main__":
    play()
