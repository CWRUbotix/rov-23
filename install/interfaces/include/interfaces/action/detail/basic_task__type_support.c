// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from interfaces:action/BasicTask.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "interfaces/action/detail/basic_task__rosidl_typesupport_introspection_c.h"
#include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "interfaces/action/detail/basic_task__functions.h"
#include "interfaces/action/detail/basic_task__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void BasicTask_Goal__rosidl_typesupport_introspection_c__BasicTask_Goal_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  interfaces__action__BasicTask_Goal__init(message_memory);
}

void BasicTask_Goal__rosidl_typesupport_introspection_c__BasicTask_Goal_fini_function(void * message_memory)
{
  interfaces__action__BasicTask_Goal__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember BasicTask_Goal__rosidl_typesupport_introspection_c__BasicTask_Goal_message_member_array[1] = {
  {
    "structure_needs_at_least_one_member",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__BasicTask_Goal, structure_needs_at_least_one_member),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers BasicTask_Goal__rosidl_typesupport_introspection_c__BasicTask_Goal_message_members = {
  "interfaces__action",  // message namespace
  "BasicTask_Goal",  // message name
  1,  // number of fields
  sizeof(interfaces__action__BasicTask_Goal),
  BasicTask_Goal__rosidl_typesupport_introspection_c__BasicTask_Goal_message_member_array,  // message members
  BasicTask_Goal__rosidl_typesupport_introspection_c__BasicTask_Goal_init_function,  // function to initialize message memory (memory has to be allocated)
  BasicTask_Goal__rosidl_typesupport_introspection_c__BasicTask_Goal_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t BasicTask_Goal__rosidl_typesupport_introspection_c__BasicTask_Goal_message_type_support_handle = {
  0,
  &BasicTask_Goal__rosidl_typesupport_introspection_c__BasicTask_Goal_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, BasicTask_Goal)() {
  if (!BasicTask_Goal__rosidl_typesupport_introspection_c__BasicTask_Goal_message_type_support_handle.typesupport_identifier) {
    BasicTask_Goal__rosidl_typesupport_introspection_c__BasicTask_Goal_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &BasicTask_Goal__rosidl_typesupport_introspection_c__BasicTask_Goal_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/action/detail/basic_task__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/action/detail/basic_task__functions.h"
// already included above
// #include "interfaces/action/detail/basic_task__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void BasicTask_Result__rosidl_typesupport_introspection_c__BasicTask_Result_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  interfaces__action__BasicTask_Result__init(message_memory);
}

void BasicTask_Result__rosidl_typesupport_introspection_c__BasicTask_Result_fini_function(void * message_memory)
{
  interfaces__action__BasicTask_Result__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember BasicTask_Result__rosidl_typesupport_introspection_c__BasicTask_Result_message_member_array[1] = {
  {
    "structure_needs_at_least_one_member",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__BasicTask_Result, structure_needs_at_least_one_member),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers BasicTask_Result__rosidl_typesupport_introspection_c__BasicTask_Result_message_members = {
  "interfaces__action",  // message namespace
  "BasicTask_Result",  // message name
  1,  // number of fields
  sizeof(interfaces__action__BasicTask_Result),
  BasicTask_Result__rosidl_typesupport_introspection_c__BasicTask_Result_message_member_array,  // message members
  BasicTask_Result__rosidl_typesupport_introspection_c__BasicTask_Result_init_function,  // function to initialize message memory (memory has to be allocated)
  BasicTask_Result__rosidl_typesupport_introspection_c__BasicTask_Result_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t BasicTask_Result__rosidl_typesupport_introspection_c__BasicTask_Result_message_type_support_handle = {
  0,
  &BasicTask_Result__rosidl_typesupport_introspection_c__BasicTask_Result_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, BasicTask_Result)() {
  if (!BasicTask_Result__rosidl_typesupport_introspection_c__BasicTask_Result_message_type_support_handle.typesupport_identifier) {
    BasicTask_Result__rosidl_typesupport_introspection_c__BasicTask_Result_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &BasicTask_Result__rosidl_typesupport_introspection_c__BasicTask_Result_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/action/detail/basic_task__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/action/detail/basic_task__functions.h"
// already included above
// #include "interfaces/action/detail/basic_task__struct.h"


// Include directives for member types
// Member `feedback_message`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void BasicTask_Feedback__rosidl_typesupport_introspection_c__BasicTask_Feedback_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  interfaces__action__BasicTask_Feedback__init(message_memory);
}

void BasicTask_Feedback__rosidl_typesupport_introspection_c__BasicTask_Feedback_fini_function(void * message_memory)
{
  interfaces__action__BasicTask_Feedback__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember BasicTask_Feedback__rosidl_typesupport_introspection_c__BasicTask_Feedback_message_member_array[1] = {
  {
    "feedback_message",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__BasicTask_Feedback, feedback_message),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers BasicTask_Feedback__rosidl_typesupport_introspection_c__BasicTask_Feedback_message_members = {
  "interfaces__action",  // message namespace
  "BasicTask_Feedback",  // message name
  1,  // number of fields
  sizeof(interfaces__action__BasicTask_Feedback),
  BasicTask_Feedback__rosidl_typesupport_introspection_c__BasicTask_Feedback_message_member_array,  // message members
  BasicTask_Feedback__rosidl_typesupport_introspection_c__BasicTask_Feedback_init_function,  // function to initialize message memory (memory has to be allocated)
  BasicTask_Feedback__rosidl_typesupport_introspection_c__BasicTask_Feedback_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t BasicTask_Feedback__rosidl_typesupport_introspection_c__BasicTask_Feedback_message_type_support_handle = {
  0,
  &BasicTask_Feedback__rosidl_typesupport_introspection_c__BasicTask_Feedback_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, BasicTask_Feedback)() {
  if (!BasicTask_Feedback__rosidl_typesupport_introspection_c__BasicTask_Feedback_message_type_support_handle.typesupport_identifier) {
    BasicTask_Feedback__rosidl_typesupport_introspection_c__BasicTask_Feedback_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &BasicTask_Feedback__rosidl_typesupport_introspection_c__BasicTask_Feedback_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/action/detail/basic_task__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/action/detail/basic_task__functions.h"
// already included above
// #include "interfaces/action/detail/basic_task__struct.h"


// Include directives for member types
// Member `goal_id`
#include "unique_identifier_msgs/msg/uuid.h"
// Member `goal_id`
#include "unique_identifier_msgs/msg/detail/uuid__rosidl_typesupport_introspection_c.h"
// Member `goal`
#include "interfaces/action/basic_task.h"
// Member `goal`
// already included above
// #include "interfaces/action/detail/basic_task__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void BasicTask_SendGoal_Request__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  interfaces__action__BasicTask_SendGoal_Request__init(message_memory);
}

void BasicTask_SendGoal_Request__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Request_fini_function(void * message_memory)
{
  interfaces__action__BasicTask_SendGoal_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember BasicTask_SendGoal_Request__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Request_message_member_array[2] = {
  {
    "goal_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__BasicTask_SendGoal_Request, goal_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "goal",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__BasicTask_SendGoal_Request, goal),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers BasicTask_SendGoal_Request__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Request_message_members = {
  "interfaces__action",  // message namespace
  "BasicTask_SendGoal_Request",  // message name
  2,  // number of fields
  sizeof(interfaces__action__BasicTask_SendGoal_Request),
  BasicTask_SendGoal_Request__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Request_message_member_array,  // message members
  BasicTask_SendGoal_Request__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  BasicTask_SendGoal_Request__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t BasicTask_SendGoal_Request__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Request_message_type_support_handle = {
  0,
  &BasicTask_SendGoal_Request__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, BasicTask_SendGoal_Request)() {
  BasicTask_SendGoal_Request__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Request_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, unique_identifier_msgs, msg, UUID)();
  BasicTask_SendGoal_Request__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Request_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, BasicTask_Goal)();
  if (!BasicTask_SendGoal_Request__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Request_message_type_support_handle.typesupport_identifier) {
    BasicTask_SendGoal_Request__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &BasicTask_SendGoal_Request__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/action/detail/basic_task__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/action/detail/basic_task__functions.h"
// already included above
// #include "interfaces/action/detail/basic_task__struct.h"


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/time.h"
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void BasicTask_SendGoal_Response__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  interfaces__action__BasicTask_SendGoal_Response__init(message_memory);
}

void BasicTask_SendGoal_Response__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Response_fini_function(void * message_memory)
{
  interfaces__action__BasicTask_SendGoal_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember BasicTask_SendGoal_Response__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Response_message_member_array[2] = {
  {
    "accepted",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__BasicTask_SendGoal_Response, accepted),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "stamp",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__BasicTask_SendGoal_Response, stamp),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers BasicTask_SendGoal_Response__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Response_message_members = {
  "interfaces__action",  // message namespace
  "BasicTask_SendGoal_Response",  // message name
  2,  // number of fields
  sizeof(interfaces__action__BasicTask_SendGoal_Response),
  BasicTask_SendGoal_Response__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Response_message_member_array,  // message members
  BasicTask_SendGoal_Response__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  BasicTask_SendGoal_Response__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t BasicTask_SendGoal_Response__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Response_message_type_support_handle = {
  0,
  &BasicTask_SendGoal_Response__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, BasicTask_SendGoal_Response)() {
  BasicTask_SendGoal_Response__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Response_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, builtin_interfaces, msg, Time)();
  if (!BasicTask_SendGoal_Response__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Response_message_type_support_handle.typesupport_identifier) {
    BasicTask_SendGoal_Response__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &BasicTask_SendGoal_Response__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "interfaces/action/detail/basic_task__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers interfaces__action__detail__basic_task__rosidl_typesupport_introspection_c__BasicTask_SendGoal_service_members = {
  "interfaces__action",  // service namespace
  "BasicTask_SendGoal",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // interfaces__action__detail__basic_task__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Request_message_type_support_handle,
  NULL  // response message
  // interfaces__action__detail__basic_task__rosidl_typesupport_introspection_c__BasicTask_SendGoal_Response_message_type_support_handle
};

static rosidl_service_type_support_t interfaces__action__detail__basic_task__rosidl_typesupport_introspection_c__BasicTask_SendGoal_service_type_support_handle = {
  0,
  &interfaces__action__detail__basic_task__rosidl_typesupport_introspection_c__BasicTask_SendGoal_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, BasicTask_SendGoal_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, BasicTask_SendGoal_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, BasicTask_SendGoal)() {
  if (!interfaces__action__detail__basic_task__rosidl_typesupport_introspection_c__BasicTask_SendGoal_service_type_support_handle.typesupport_identifier) {
    interfaces__action__detail__basic_task__rosidl_typesupport_introspection_c__BasicTask_SendGoal_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)interfaces__action__detail__basic_task__rosidl_typesupport_introspection_c__BasicTask_SendGoal_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, BasicTask_SendGoal_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, BasicTask_SendGoal_Response)()->data;
  }

  return &interfaces__action__detail__basic_task__rosidl_typesupport_introspection_c__BasicTask_SendGoal_service_type_support_handle;
}

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/action/detail/basic_task__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/action/detail/basic_task__functions.h"
// already included above
// #include "interfaces/action/detail/basic_task__struct.h"


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/uuid.h"
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void BasicTask_GetResult_Request__rosidl_typesupport_introspection_c__BasicTask_GetResult_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  interfaces__action__BasicTask_GetResult_Request__init(message_memory);
}

void BasicTask_GetResult_Request__rosidl_typesupport_introspection_c__BasicTask_GetResult_Request_fini_function(void * message_memory)
{
  interfaces__action__BasicTask_GetResult_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember BasicTask_GetResult_Request__rosidl_typesupport_introspection_c__BasicTask_GetResult_Request_message_member_array[1] = {
  {
    "goal_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__BasicTask_GetResult_Request, goal_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers BasicTask_GetResult_Request__rosidl_typesupport_introspection_c__BasicTask_GetResult_Request_message_members = {
  "interfaces__action",  // message namespace
  "BasicTask_GetResult_Request",  // message name
  1,  // number of fields
  sizeof(interfaces__action__BasicTask_GetResult_Request),
  BasicTask_GetResult_Request__rosidl_typesupport_introspection_c__BasicTask_GetResult_Request_message_member_array,  // message members
  BasicTask_GetResult_Request__rosidl_typesupport_introspection_c__BasicTask_GetResult_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  BasicTask_GetResult_Request__rosidl_typesupport_introspection_c__BasicTask_GetResult_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t BasicTask_GetResult_Request__rosidl_typesupport_introspection_c__BasicTask_GetResult_Request_message_type_support_handle = {
  0,
  &BasicTask_GetResult_Request__rosidl_typesupport_introspection_c__BasicTask_GetResult_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, BasicTask_GetResult_Request)() {
  BasicTask_GetResult_Request__rosidl_typesupport_introspection_c__BasicTask_GetResult_Request_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, unique_identifier_msgs, msg, UUID)();
  if (!BasicTask_GetResult_Request__rosidl_typesupport_introspection_c__BasicTask_GetResult_Request_message_type_support_handle.typesupport_identifier) {
    BasicTask_GetResult_Request__rosidl_typesupport_introspection_c__BasicTask_GetResult_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &BasicTask_GetResult_Request__rosidl_typesupport_introspection_c__BasicTask_GetResult_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/action/detail/basic_task__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/action/detail/basic_task__functions.h"
// already included above
// #include "interfaces/action/detail/basic_task__struct.h"


// Include directives for member types
// Member `result`
// already included above
// #include "interfaces/action/basic_task.h"
// Member `result`
// already included above
// #include "interfaces/action/detail/basic_task__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void BasicTask_GetResult_Response__rosidl_typesupport_introspection_c__BasicTask_GetResult_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  interfaces__action__BasicTask_GetResult_Response__init(message_memory);
}

void BasicTask_GetResult_Response__rosidl_typesupport_introspection_c__BasicTask_GetResult_Response_fini_function(void * message_memory)
{
  interfaces__action__BasicTask_GetResult_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember BasicTask_GetResult_Response__rosidl_typesupport_introspection_c__BasicTask_GetResult_Response_message_member_array[2] = {
  {
    "status",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__BasicTask_GetResult_Response, status),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "result",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__BasicTask_GetResult_Response, result),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers BasicTask_GetResult_Response__rosidl_typesupport_introspection_c__BasicTask_GetResult_Response_message_members = {
  "interfaces__action",  // message namespace
  "BasicTask_GetResult_Response",  // message name
  2,  // number of fields
  sizeof(interfaces__action__BasicTask_GetResult_Response),
  BasicTask_GetResult_Response__rosidl_typesupport_introspection_c__BasicTask_GetResult_Response_message_member_array,  // message members
  BasicTask_GetResult_Response__rosidl_typesupport_introspection_c__BasicTask_GetResult_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  BasicTask_GetResult_Response__rosidl_typesupport_introspection_c__BasicTask_GetResult_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t BasicTask_GetResult_Response__rosidl_typesupport_introspection_c__BasicTask_GetResult_Response_message_type_support_handle = {
  0,
  &BasicTask_GetResult_Response__rosidl_typesupport_introspection_c__BasicTask_GetResult_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, BasicTask_GetResult_Response)() {
  BasicTask_GetResult_Response__rosidl_typesupport_introspection_c__BasicTask_GetResult_Response_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, BasicTask_Result)();
  if (!BasicTask_GetResult_Response__rosidl_typesupport_introspection_c__BasicTask_GetResult_Response_message_type_support_handle.typesupport_identifier) {
    BasicTask_GetResult_Response__rosidl_typesupport_introspection_c__BasicTask_GetResult_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &BasicTask_GetResult_Response__rosidl_typesupport_introspection_c__BasicTask_GetResult_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "interfaces/action/detail/basic_task__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers interfaces__action__detail__basic_task__rosidl_typesupport_introspection_c__BasicTask_GetResult_service_members = {
  "interfaces__action",  // service namespace
  "BasicTask_GetResult",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // interfaces__action__detail__basic_task__rosidl_typesupport_introspection_c__BasicTask_GetResult_Request_message_type_support_handle,
  NULL  // response message
  // interfaces__action__detail__basic_task__rosidl_typesupport_introspection_c__BasicTask_GetResult_Response_message_type_support_handle
};

static rosidl_service_type_support_t interfaces__action__detail__basic_task__rosidl_typesupport_introspection_c__BasicTask_GetResult_service_type_support_handle = {
  0,
  &interfaces__action__detail__basic_task__rosidl_typesupport_introspection_c__BasicTask_GetResult_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, BasicTask_GetResult_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, BasicTask_GetResult_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, BasicTask_GetResult)() {
  if (!interfaces__action__detail__basic_task__rosidl_typesupport_introspection_c__BasicTask_GetResult_service_type_support_handle.typesupport_identifier) {
    interfaces__action__detail__basic_task__rosidl_typesupport_introspection_c__BasicTask_GetResult_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)interfaces__action__detail__basic_task__rosidl_typesupport_introspection_c__BasicTask_GetResult_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, BasicTask_GetResult_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, BasicTask_GetResult_Response)()->data;
  }

  return &interfaces__action__detail__basic_task__rosidl_typesupport_introspection_c__BasicTask_GetResult_service_type_support_handle;
}

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/action/detail/basic_task__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/action/detail/basic_task__functions.h"
// already included above
// #include "interfaces/action/detail/basic_task__struct.h"


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/uuid.h"
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__rosidl_typesupport_introspection_c.h"
// Member `feedback`
// already included above
// #include "interfaces/action/basic_task.h"
// Member `feedback`
// already included above
// #include "interfaces/action/detail/basic_task__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void BasicTask_FeedbackMessage__rosidl_typesupport_introspection_c__BasicTask_FeedbackMessage_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  interfaces__action__BasicTask_FeedbackMessage__init(message_memory);
}

void BasicTask_FeedbackMessage__rosidl_typesupport_introspection_c__BasicTask_FeedbackMessage_fini_function(void * message_memory)
{
  interfaces__action__BasicTask_FeedbackMessage__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember BasicTask_FeedbackMessage__rosidl_typesupport_introspection_c__BasicTask_FeedbackMessage_message_member_array[2] = {
  {
    "goal_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__BasicTask_FeedbackMessage, goal_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "feedback",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__BasicTask_FeedbackMessage, feedback),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers BasicTask_FeedbackMessage__rosidl_typesupport_introspection_c__BasicTask_FeedbackMessage_message_members = {
  "interfaces__action",  // message namespace
  "BasicTask_FeedbackMessage",  // message name
  2,  // number of fields
  sizeof(interfaces__action__BasicTask_FeedbackMessage),
  BasicTask_FeedbackMessage__rosidl_typesupport_introspection_c__BasicTask_FeedbackMessage_message_member_array,  // message members
  BasicTask_FeedbackMessage__rosidl_typesupport_introspection_c__BasicTask_FeedbackMessage_init_function,  // function to initialize message memory (memory has to be allocated)
  BasicTask_FeedbackMessage__rosidl_typesupport_introspection_c__BasicTask_FeedbackMessage_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t BasicTask_FeedbackMessage__rosidl_typesupport_introspection_c__BasicTask_FeedbackMessage_message_type_support_handle = {
  0,
  &BasicTask_FeedbackMessage__rosidl_typesupport_introspection_c__BasicTask_FeedbackMessage_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, BasicTask_FeedbackMessage)() {
  BasicTask_FeedbackMessage__rosidl_typesupport_introspection_c__BasicTask_FeedbackMessage_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, unique_identifier_msgs, msg, UUID)();
  BasicTask_FeedbackMessage__rosidl_typesupport_introspection_c__BasicTask_FeedbackMessage_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, BasicTask_Feedback)();
  if (!BasicTask_FeedbackMessage__rosidl_typesupport_introspection_c__BasicTask_FeedbackMessage_message_type_support_handle.typesupport_identifier) {
    BasicTask_FeedbackMessage__rosidl_typesupport_introspection_c__BasicTask_FeedbackMessage_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &BasicTask_FeedbackMessage__rosidl_typesupport_introspection_c__BasicTask_FeedbackMessage_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
