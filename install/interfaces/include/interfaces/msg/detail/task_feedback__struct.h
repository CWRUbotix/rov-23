// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:msg/TaskFeedback.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__TASK_FEEDBACK__STRUCT_H_
#define INTERFACES__MSG__DETAIL__TASK_FEEDBACK__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/TaskFeedback in the package interfaces.
typedef struct interfaces__msg__TaskFeedback
{
  int64_t task_id;
} interfaces__msg__TaskFeedback;

// Struct for a sequence of interfaces__msg__TaskFeedback.
typedef struct interfaces__msg__TaskFeedback__Sequence
{
  interfaces__msg__TaskFeedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__msg__TaskFeedback__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__MSG__DETAIL__TASK_FEEDBACK__STRUCT_H_
