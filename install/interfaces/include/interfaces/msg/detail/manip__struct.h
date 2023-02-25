// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:msg/Manip.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__MANIP__STRUCT_H_
#define INTERFACES__MSG__DETAIL__MANIP__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'manip_id'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/Manip in the package interfaces.
typedef struct interfaces__msg__Manip
{
  rosidl_runtime_c__String manip_id;
  bool activated;
} interfaces__msg__Manip;

// Struct for a sequence of interfaces__msg__Manip.
typedef struct interfaces__msg__Manip__Sequence
{
  interfaces__msg__Manip * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__msg__Manip__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__MSG__DETAIL__MANIP__STRUCT_H_
