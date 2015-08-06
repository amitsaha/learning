enum SexType {
  MALE = 1,
  FEMALE = 2
}

struct User {
  1: string firstname,
  2: string lastname,
  3: i32 user_id = 0, /*32-bit signed integer, i64 - 64 bit signed integer*/
  4: SexType sex,
  5: bool active = false,
  6: optional string description
}

exception InvalidValueException {
  1: i32 error_code,
  2: string error_msg
}

service UserExchange {
  void ping(),
  i32 add_user(1:User u) throws (1: InvalidValueException e),
  User get_user(1:i32 uid) throws (1: InvalidValueException e),
  oneway void clear_list()
}
