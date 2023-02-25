// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:msg/ROVControl.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__ROV_CONTROL__STRUCT_H_
#define INTERFACES__MSG__DETAIL__ROV_CONTROL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

// Struct defined in msg/ROVControl in the package interfaces.
typedef struct interfaces__msg__ROVControl
{
  std_msgs__msg__Header header;
  int16_t x;
  int16_t y;
  int16_t z;
  int16_t yaw;
  int16_t pitch;
  int16_t roll;
} interfaces__msg__ROVControl;

// Struct for a sequence of interfaces__msg__ROVControl.
typedef struct interfaces__msg__ROVControl__Sequence
{
  interfaces__msg__ROVControl * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__msg__ROVControl__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__MSG__DETAIL__ROV_CONTROL__STRUCT_H_
