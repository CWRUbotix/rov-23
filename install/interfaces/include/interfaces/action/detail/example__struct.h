// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:action/Example.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__ACTION__DETAIL__EXAMPLE__STRUCT_H_
#define INTERFACES__ACTION__DETAIL__EXAMPLE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in action/Example in the package interfaces.
typedef struct interfaces__action__Example_Goal
{
  bool morning;
  bool cheery;
} interfaces__action__Example_Goal;

// Struct for a sequence of interfaces__action__Example_Goal.
typedef struct interfaces__action__Example_Goal__Sequence
{
  interfaces__action__Example_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__action__Example_Goal__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'message'
#include "rosidl_runtime_c/string.h"

// Struct defined in action/Example in the package interfaces.
typedef struct interfaces__action__Example_Result
{
  rosidl_runtime_c__String message;
} interfaces__action__Example_Result;

// Struct for a sequence of interfaces__action__Example_Result.
typedef struct interfaces__action__Example_Result__Sequence
{
  interfaces__action__Example_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__action__Example_Result__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'feedback_message'
// already included above
// #include "rosidl_runtime_c/string.h"

// Struct defined in action/Example in the package interfaces.
typedef struct interfaces__action__Example_Feedback
{
  rosidl_runtime_c__String feedback_message;
} interfaces__action__Example_Feedback;

// Struct for a sequence of interfaces__action__Example_Feedback.
typedef struct interfaces__action__Example_Feedback__Sequence
{
  interfaces__action__Example_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__action__Example_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "interfaces/action/detail/example__struct.h"

// Struct defined in action/Example in the package interfaces.
typedef struct interfaces__action__Example_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  interfaces__action__Example_Goal goal;
} interfaces__action__Example_SendGoal_Request;

// Struct for a sequence of interfaces__action__Example_SendGoal_Request.
typedef struct interfaces__action__Example_SendGoal_Request__Sequence
{
  interfaces__action__Example_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__action__Example_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

// Struct defined in action/Example in the package interfaces.
typedef struct interfaces__action__Example_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} interfaces__action__Example_SendGoal_Response;

// Struct for a sequence of interfaces__action__Example_SendGoal_Response.
typedef struct interfaces__action__Example_SendGoal_Response__Sequence
{
  interfaces__action__Example_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__action__Example_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

// Struct defined in action/Example in the package interfaces.
typedef struct interfaces__action__Example_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} interfaces__action__Example_GetResult_Request;

// Struct for a sequence of interfaces__action__Example_GetResult_Request.
typedef struct interfaces__action__Example_GetResult_Request__Sequence
{
  interfaces__action__Example_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__action__Example_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "interfaces/action/detail/example__struct.h"

// Struct defined in action/Example in the package interfaces.
typedef struct interfaces__action__Example_GetResult_Response
{
  int8_t status;
  interfaces__action__Example_Result result;
} interfaces__action__Example_GetResult_Response;

// Struct for a sequence of interfaces__action__Example_GetResult_Response.
typedef struct interfaces__action__Example_GetResult_Response__Sequence
{
  interfaces__action__Example_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__action__Example_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "interfaces/action/detail/example__struct.h"

// Struct defined in action/Example in the package interfaces.
typedef struct interfaces__action__Example_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  interfaces__action__Example_Feedback feedback;
} interfaces__action__Example_FeedbackMessage;

// Struct for a sequence of interfaces__action__Example_FeedbackMessage.
typedef struct interfaces__action__Example_FeedbackMessage__Sequence
{
  interfaces__action__Example_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__action__Example_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__ACTION__DETAIL__EXAMPLE__STRUCT_H_
