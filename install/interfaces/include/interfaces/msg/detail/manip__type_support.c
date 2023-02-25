// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from interfaces:msg/Manip.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "interfaces/msg/detail/manip__rosidl_typesupport_introspection_c.h"
#include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "interfaces/msg/detail/manip__functions.h"
#include "interfaces/msg/detail/manip__struct.h"


// Include directives for member types
// Member `manip_id`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void Manip__rosidl_typesupport_introspection_c__Manip_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  interfaces__msg__Manip__init(message_memory);
}

void Manip__rosidl_typesupport_introspection_c__Manip_fini_function(void * message_memory)
{
  interfaces__msg__Manip__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember Manip__rosidl_typesupport_introspection_c__Manip_message_member_array[2] = {
  {
    "manip_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__msg__Manip, manip_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "activated",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__msg__Manip, activated),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Manip__rosidl_typesupport_introspection_c__Manip_message_members = {
  "interfaces__msg",  // message namespace
  "Manip",  // message name
  2,  // number of fields
  sizeof(interfaces__msg__Manip),
  Manip__rosidl_typesupport_introspection_c__Manip_message_member_array,  // message members
  Manip__rosidl_typesupport_introspection_c__Manip_init_function,  // function to initialize message memory (memory has to be allocated)
  Manip__rosidl_typesupport_introspection_c__Manip_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Manip__rosidl_typesupport_introspection_c__Manip_message_type_support_handle = {
  0,
  &Manip__rosidl_typesupport_introspection_c__Manip_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, msg, Manip)() {
  if (!Manip__rosidl_typesupport_introspection_c__Manip_message_type_support_handle.typesupport_identifier) {
    Manip__rosidl_typesupport_introspection_c__Manip_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Manip__rosidl_typesupport_introspection_c__Manip_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
