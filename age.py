driving = input("請問你有沒有開過車?:")
if driving != "有" and driving != "沒有":
	print("只能輸入 有/沒有")
	raise SystemExit

age = int(input("請問你的年齡? "))
if driving == "有":
	if age >= 18:
		print("恭喜你通過測驗了")
	else:
		print("奇怪，你怎麼會開過車")
elif driving == "沒有":
	if age >= 18:
		print("你可以準備去考駕照拉")
	else:
		print("等到18歲就可以去考駕照了")
