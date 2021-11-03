class Human:
  name = ["佐藤", "田中", "鈴木", "山田", "リオン"]

class Patient(Human):
  symptom = ["咳", "腹痛", "鼻水", "倦怠感", "鼻づまり"]
  patient_id = [111, 222, 333, 444, 555]


class Clinic:
  patient_list = []

  def show_wating_count():
    Human.count

  def reserve():
    if _check_reserved() == True:
      print("予約済みです")

  def diagnosis():
  
  def _check_reserved():
    return True