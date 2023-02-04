// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from interfaces:action/BasicTask.idl
// generated code does not contain a copyright notice
#include "interfaces/action/detail/basic_task__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


bool
interfaces__action__BasicTask_Goal__init(interfaces__action__BasicTask_Goal * msg)
{
  if (!msg) {
    return false;
  }
  // structure_needs_at_least_one_member
  return true;
}

void
interfaces__action__BasicTask_Goal__fini(interfaces__action__BasicTask_Goal * msg)
{
  if (!msg) {
    return;
  }
  // structure_needs_at_least_one_member
}

bool
interfaces__action__BasicTask_Goal__are_equal(const interfaces__action__BasicTask_Goal * lhs, const interfaces__action__BasicTask_Goal * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // structure_needs_at_least_one_member
  if (lhs->structure_needs_at_least_one_member != rhs->structure_needs_at_least_one_member) {
    return false;
  }
  return true;
}

bool
interfaces__action__BasicTask_Goal__copy(
  const interfaces__action__BasicTask_Goal * input,
  interfaces__action__BasicTask_Goal * output)
{
  if (!input || !output) {
    return false;
  }
  // structure_needs_at_least_one_member
  output->structure_needs_at_least_one_member = input->structure_needs_at_least_one_member;
  return true;
}

interfaces__action__BasicTask_Goal *
interfaces__action__BasicTask_Goal__create()
{
  interfaces__action__BasicTask_Goal * msg = (interfaces__action__BasicTask_Goal *)malloc(sizeof(interfaces__action__BasicTask_Goal));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__action__BasicTask_Goal));
  bool success = interfaces__action__BasicTask_Goal__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interfaces__action__BasicTask_Goal__destroy(interfaces__action__BasicTask_Goal * msg)
{
  if (msg) {
    interfaces__action__BasicTask_Goal__fini(msg);
  }
  free(msg);
}


bool
interfaces__action__BasicTask_Goal__Sequence__init(interfaces__action__BasicTask_Goal__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interfaces__action__BasicTask_Goal * data = NULL;
  if (size) {
    data = (interfaces__action__BasicTask_Goal *)calloc(size, sizeof(interfaces__action__BasicTask_Goal));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__action__BasicTask_Goal__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__action__BasicTask_Goal__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
interfaces__action__BasicTask_Goal__Sequence__fini(interfaces__action__BasicTask_Goal__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__action__BasicTask_Goal__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

interfaces__action__BasicTask_Goal__Sequence *
interfaces__action__BasicTask_Goal__Sequence__create(size_t size)
{
  interfaces__action__BasicTask_Goal__Sequence * array = (interfaces__action__BasicTask_Goal__Sequence *)malloc(sizeof(interfaces__action__BasicTask_Goal__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interfaces__action__BasicTask_Goal__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interfaces__action__BasicTask_Goal__Sequence__destroy(interfaces__action__BasicTask_Goal__Sequence * array)
{
  if (array) {
    interfaces__action__BasicTask_Goal__Sequence__fini(array);
  }
  free(array);
}

bool
interfaces__action__BasicTask_Goal__Sequence__are_equal(const interfaces__action__BasicTask_Goal__Sequence * lhs, const interfaces__action__BasicTask_Goal__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!interfaces__action__BasicTask_Goal__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
interfaces__action__BasicTask_Goal__Sequence__copy(
  const interfaces__action__BasicTask_Goal__Sequence * input,
  interfaces__action__BasicTask_Goal__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(interfaces__action__BasicTask_Goal);
    interfaces__action__BasicTask_Goal * data =
      (interfaces__action__BasicTask_Goal *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!interfaces__action__BasicTask_Goal__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          interfaces__action__BasicTask_Goal__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!interfaces__action__BasicTask_Goal__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
interfaces__action__BasicTask_Result__init(interfaces__action__BasicTask_Result * msg)
{
  if (!msg) {
    return false;
  }
  // structure_needs_at_least_one_member
  return true;
}

void
interfaces__action__BasicTask_Result__fini(interfaces__action__BasicTask_Result * msg)
{
  if (!msg) {
    return;
  }
  // structure_needs_at_least_one_member
}

bool
interfaces__action__BasicTask_Result__are_equal(const interfaces__action__BasicTask_Result * lhs, const interfaces__action__BasicTask_Result * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // structure_needs_at_least_one_member
  if (lhs->structure_needs_at_least_one_member != rhs->structure_needs_at_least_one_member) {
    return false;
  }
  return true;
}

bool
interfaces__action__BasicTask_Result__copy(
  const interfaces__action__BasicTask_Result * input,
  interfaces__action__BasicTask_Result * output)
{
  if (!input || !output) {
    return false;
  }
  // structure_needs_at_least_one_member
  output->structure_needs_at_least_one_member = input->structure_needs_at_least_one_member;
  return true;
}

interfaces__action__BasicTask_Result *
interfaces__action__BasicTask_Result__create()
{
  interfaces__action__BasicTask_Result * msg = (interfaces__action__BasicTask_Result *)malloc(sizeof(interfaces__action__BasicTask_Result));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__action__BasicTask_Result));
  bool success = interfaces__action__BasicTask_Result__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interfaces__action__BasicTask_Result__destroy(interfaces__action__BasicTask_Result * msg)
{
  if (msg) {
    interfaces__action__BasicTask_Result__fini(msg);
  }
  free(msg);
}


bool
interfaces__action__BasicTask_Result__Sequence__init(interfaces__action__BasicTask_Result__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interfaces__action__BasicTask_Result * data = NULL;
  if (size) {
    data = (interfaces__action__BasicTask_Result *)calloc(size, sizeof(interfaces__action__BasicTask_Result));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__action__BasicTask_Result__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__action__BasicTask_Result__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
interfaces__action__BasicTask_Result__Sequence__fini(interfaces__action__BasicTask_Result__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__action__BasicTask_Result__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

interfaces__action__BasicTask_Result__Sequence *
interfaces__action__BasicTask_Result__Sequence__create(size_t size)
{
  interfaces__action__BasicTask_Result__Sequence * array = (interfaces__action__BasicTask_Result__Sequence *)malloc(sizeof(interfaces__action__BasicTask_Result__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interfaces__action__BasicTask_Result__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interfaces__action__BasicTask_Result__Sequence__destroy(interfaces__action__BasicTask_Result__Sequence * array)
{
  if (array) {
    interfaces__action__BasicTask_Result__Sequence__fini(array);
  }
  free(array);
}

bool
interfaces__action__BasicTask_Result__Sequence__are_equal(const interfaces__action__BasicTask_Result__Sequence * lhs, const interfaces__action__BasicTask_Result__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!interfaces__action__BasicTask_Result__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
interfaces__action__BasicTask_Result__Sequence__copy(
  const interfaces__action__BasicTask_Result__Sequence * input,
  interfaces__action__BasicTask_Result__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(interfaces__action__BasicTask_Result);
    interfaces__action__BasicTask_Result * data =
      (interfaces__action__BasicTask_Result *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!interfaces__action__BasicTask_Result__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          interfaces__action__BasicTask_Result__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!interfaces__action__BasicTask_Result__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `feedback_message`
#include "rosidl_runtime_c/string_functions.h"

bool
interfaces__action__BasicTask_Feedback__init(interfaces__action__BasicTask_Feedback * msg)
{
  if (!msg) {
    return false;
  }
  // feedback_message
  if (!rosidl_runtime_c__String__init(&msg->feedback_message)) {
    interfaces__action__BasicTask_Feedback__fini(msg);
    return false;
  }
  return true;
}

void
interfaces__action__BasicTask_Feedback__fini(interfaces__action__BasicTask_Feedback * msg)
{
  if (!msg) {
    return;
  }
  // feedback_message
  rosidl_runtime_c__String__fini(&msg->feedback_message);
}

bool
interfaces__action__BasicTask_Feedback__are_equal(const interfaces__action__BasicTask_Feedback * lhs, const interfaces__action__BasicTask_Feedback * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // feedback_message
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->feedback_message), &(rhs->feedback_message)))
  {
    return false;
  }
  return true;
}

bool
interfaces__action__BasicTask_Feedback__copy(
  const interfaces__action__BasicTask_Feedback * input,
  interfaces__action__BasicTask_Feedback * output)
{
  if (!input || !output) {
    return false;
  }
  // feedback_message
  if (!rosidl_runtime_c__String__copy(
      &(input->feedback_message), &(output->feedback_message)))
  {
    return false;
  }
  return true;
}

interfaces__action__BasicTask_Feedback *
interfaces__action__BasicTask_Feedback__create()
{
  interfaces__action__BasicTask_Feedback * msg = (interfaces__action__BasicTask_Feedback *)malloc(sizeof(interfaces__action__BasicTask_Feedback));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__action__BasicTask_Feedback));
  bool success = interfaces__action__BasicTask_Feedback__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interfaces__action__BasicTask_Feedback__destroy(interfaces__action__BasicTask_Feedback * msg)
{
  if (msg) {
    interfaces__action__BasicTask_Feedback__fini(msg);
  }
  free(msg);
}


bool
interfaces__action__BasicTask_Feedback__Sequence__init(interfaces__action__BasicTask_Feedback__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interfaces__action__BasicTask_Feedback * data = NULL;
  if (size) {
    data = (interfaces__action__BasicTask_Feedback *)calloc(size, sizeof(interfaces__action__BasicTask_Feedback));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__action__BasicTask_Feedback__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__action__BasicTask_Feedback__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
interfaces__action__BasicTask_Feedback__Sequence__fini(interfaces__action__BasicTask_Feedback__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__action__BasicTask_Feedback__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

interfaces__action__BasicTask_Feedback__Sequence *
interfaces__action__BasicTask_Feedback__Sequence__create(size_t size)
{
  interfaces__action__BasicTask_Feedback__Sequence * array = (interfaces__action__BasicTask_Feedback__Sequence *)malloc(sizeof(interfaces__action__BasicTask_Feedback__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interfaces__action__BasicTask_Feedback__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interfaces__action__BasicTask_Feedback__Sequence__destroy(interfaces__action__BasicTask_Feedback__Sequence * array)
{
  if (array) {
    interfaces__action__BasicTask_Feedback__Sequence__fini(array);
  }
  free(array);
}

bool
interfaces__action__BasicTask_Feedback__Sequence__are_equal(const interfaces__action__BasicTask_Feedback__Sequence * lhs, const interfaces__action__BasicTask_Feedback__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!interfaces__action__BasicTask_Feedback__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
interfaces__action__BasicTask_Feedback__Sequence__copy(
  const interfaces__action__BasicTask_Feedback__Sequence * input,
  interfaces__action__BasicTask_Feedback__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(interfaces__action__BasicTask_Feedback);
    interfaces__action__BasicTask_Feedback * data =
      (interfaces__action__BasicTask_Feedback *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!interfaces__action__BasicTask_Feedback__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          interfaces__action__BasicTask_Feedback__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!interfaces__action__BasicTask_Feedback__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `goal_id`
#include "unique_identifier_msgs/msg/detail/uuid__functions.h"
// Member `goal`
// already included above
// #include "interfaces/action/detail/basic_task__functions.h"

bool
interfaces__action__BasicTask_SendGoal_Request__init(interfaces__action__BasicTask_SendGoal_Request * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    interfaces__action__BasicTask_SendGoal_Request__fini(msg);
    return false;
  }
  // goal
  if (!interfaces__action__BasicTask_Goal__init(&msg->goal)) {
    interfaces__action__BasicTask_SendGoal_Request__fini(msg);
    return false;
  }
  return true;
}

void
interfaces__action__BasicTask_SendGoal_Request__fini(interfaces__action__BasicTask_SendGoal_Request * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
  // goal
  interfaces__action__BasicTask_Goal__fini(&msg->goal);
}

bool
interfaces__action__BasicTask_SendGoal_Request__are_equal(const interfaces__action__BasicTask_SendGoal_Request * lhs, const interfaces__action__BasicTask_SendGoal_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__are_equal(
      &(lhs->goal_id), &(rhs->goal_id)))
  {
    return false;
  }
  // goal
  if (!interfaces__action__BasicTask_Goal__are_equal(
      &(lhs->goal), &(rhs->goal)))
  {
    return false;
  }
  return true;
}

bool
interfaces__action__BasicTask_SendGoal_Request__copy(
  const interfaces__action__BasicTask_SendGoal_Request * input,
  interfaces__action__BasicTask_SendGoal_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__copy(
      &(input->goal_id), &(output->goal_id)))
  {
    return false;
  }
  // goal
  if (!interfaces__action__BasicTask_Goal__copy(
      &(input->goal), &(output->goal)))
  {
    return false;
  }
  return true;
}

interfaces__action__BasicTask_SendGoal_Request *
interfaces__action__BasicTask_SendGoal_Request__create()
{
  interfaces__action__BasicTask_SendGoal_Request * msg = (interfaces__action__BasicTask_SendGoal_Request *)malloc(sizeof(interfaces__action__BasicTask_SendGoal_Request));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__action__BasicTask_SendGoal_Request));
  bool success = interfaces__action__BasicTask_SendGoal_Request__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interfaces__action__BasicTask_SendGoal_Request__destroy(interfaces__action__BasicTask_SendGoal_Request * msg)
{
  if (msg) {
    interfaces__action__BasicTask_SendGoal_Request__fini(msg);
  }
  free(msg);
}


bool
interfaces__action__BasicTask_SendGoal_Request__Sequence__init(interfaces__action__BasicTask_SendGoal_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interfaces__action__BasicTask_SendGoal_Request * data = NULL;
  if (size) {
    data = (interfaces__action__BasicTask_SendGoal_Request *)calloc(size, sizeof(interfaces__action__BasicTask_SendGoal_Request));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__action__BasicTask_SendGoal_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__action__BasicTask_SendGoal_Request__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
interfaces__action__BasicTask_SendGoal_Request__Sequence__fini(interfaces__action__BasicTask_SendGoal_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__action__BasicTask_SendGoal_Request__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

interfaces__action__BasicTask_SendGoal_Request__Sequence *
interfaces__action__BasicTask_SendGoal_Request__Sequence__create(size_t size)
{
  interfaces__action__BasicTask_SendGoal_Request__Sequence * array = (interfaces__action__BasicTask_SendGoal_Request__Sequence *)malloc(sizeof(interfaces__action__BasicTask_SendGoal_Request__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interfaces__action__BasicTask_SendGoal_Request__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interfaces__action__BasicTask_SendGoal_Request__Sequence__destroy(interfaces__action__BasicTask_SendGoal_Request__Sequence * array)
{
  if (array) {
    interfaces__action__BasicTask_SendGoal_Request__Sequence__fini(array);
  }
  free(array);
}

bool
interfaces__action__BasicTask_SendGoal_Request__Sequence__are_equal(const interfaces__action__BasicTask_SendGoal_Request__Sequence * lhs, const interfaces__action__BasicTask_SendGoal_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!interfaces__action__BasicTask_SendGoal_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
interfaces__action__BasicTask_SendGoal_Request__Sequence__copy(
  const interfaces__action__BasicTask_SendGoal_Request__Sequence * input,
  interfaces__action__BasicTask_SendGoal_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(interfaces__action__BasicTask_SendGoal_Request);
    interfaces__action__BasicTask_SendGoal_Request * data =
      (interfaces__action__BasicTask_SendGoal_Request *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!interfaces__action__BasicTask_SendGoal_Request__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          interfaces__action__BasicTask_SendGoal_Request__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!interfaces__action__BasicTask_SendGoal_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__functions.h"

bool
interfaces__action__BasicTask_SendGoal_Response__init(interfaces__action__BasicTask_SendGoal_Response * msg)
{
  if (!msg) {
    return false;
  }
  // accepted
  // stamp
  if (!builtin_interfaces__msg__Time__init(&msg->stamp)) {
    interfaces__action__BasicTask_SendGoal_Response__fini(msg);
    return false;
  }
  return true;
}

void
interfaces__action__BasicTask_SendGoal_Response__fini(interfaces__action__BasicTask_SendGoal_Response * msg)
{
  if (!msg) {
    return;
  }
  // accepted
  // stamp
  builtin_interfaces__msg__Time__fini(&msg->stamp);
}

bool
interfaces__action__BasicTask_SendGoal_Response__are_equal(const interfaces__action__BasicTask_SendGoal_Response * lhs, const interfaces__action__BasicTask_SendGoal_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // accepted
  if (lhs->accepted != rhs->accepted) {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__are_equal(
      &(lhs->stamp), &(rhs->stamp)))
  {
    return false;
  }
  return true;
}

bool
interfaces__action__BasicTask_SendGoal_Response__copy(
  const interfaces__action__BasicTask_SendGoal_Response * input,
  interfaces__action__BasicTask_SendGoal_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // accepted
  output->accepted = input->accepted;
  // stamp
  if (!builtin_interfaces__msg__Time__copy(
      &(input->stamp), &(output->stamp)))
  {
    return false;
  }
  return true;
}

interfaces__action__BasicTask_SendGoal_Response *
interfaces__action__BasicTask_SendGoal_Response__create()
{
  interfaces__action__BasicTask_SendGoal_Response * msg = (interfaces__action__BasicTask_SendGoal_Response *)malloc(sizeof(interfaces__action__BasicTask_SendGoal_Response));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__action__BasicTask_SendGoal_Response));
  bool success = interfaces__action__BasicTask_SendGoal_Response__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interfaces__action__BasicTask_SendGoal_Response__destroy(interfaces__action__BasicTask_SendGoal_Response * msg)
{
  if (msg) {
    interfaces__action__BasicTask_SendGoal_Response__fini(msg);
  }
  free(msg);
}


bool
interfaces__action__BasicTask_SendGoal_Response__Sequence__init(interfaces__action__BasicTask_SendGoal_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interfaces__action__BasicTask_SendGoal_Response * data = NULL;
  if (size) {
    data = (interfaces__action__BasicTask_SendGoal_Response *)calloc(size, sizeof(interfaces__action__BasicTask_SendGoal_Response));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__action__BasicTask_SendGoal_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__action__BasicTask_SendGoal_Response__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
interfaces__action__BasicTask_SendGoal_Response__Sequence__fini(interfaces__action__BasicTask_SendGoal_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__action__BasicTask_SendGoal_Response__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

interfaces__action__BasicTask_SendGoal_Response__Sequence *
interfaces__action__BasicTask_SendGoal_Response__Sequence__create(size_t size)
{
  interfaces__action__BasicTask_SendGoal_Response__Sequence * array = (interfaces__action__BasicTask_SendGoal_Response__Sequence *)malloc(sizeof(interfaces__action__BasicTask_SendGoal_Response__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interfaces__action__BasicTask_SendGoal_Response__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interfaces__action__BasicTask_SendGoal_Response__Sequence__destroy(interfaces__action__BasicTask_SendGoal_Response__Sequence * array)
{
  if (array) {
    interfaces__action__BasicTask_SendGoal_Response__Sequence__fini(array);
  }
  free(array);
}

bool
interfaces__action__BasicTask_SendGoal_Response__Sequence__are_equal(const interfaces__action__BasicTask_SendGoal_Response__Sequence * lhs, const interfaces__action__BasicTask_SendGoal_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!interfaces__action__BasicTask_SendGoal_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
interfaces__action__BasicTask_SendGoal_Response__Sequence__copy(
  const interfaces__action__BasicTask_SendGoal_Response__Sequence * input,
  interfaces__action__BasicTask_SendGoal_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(interfaces__action__BasicTask_SendGoal_Response);
    interfaces__action__BasicTask_SendGoal_Response * data =
      (interfaces__action__BasicTask_SendGoal_Response *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!interfaces__action__BasicTask_SendGoal_Response__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          interfaces__action__BasicTask_SendGoal_Response__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!interfaces__action__BasicTask_SendGoal_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__functions.h"

bool
interfaces__action__BasicTask_GetResult_Request__init(interfaces__action__BasicTask_GetResult_Request * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    interfaces__action__BasicTask_GetResult_Request__fini(msg);
    return false;
  }
  return true;
}

void
interfaces__action__BasicTask_GetResult_Request__fini(interfaces__action__BasicTask_GetResult_Request * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
}

bool
interfaces__action__BasicTask_GetResult_Request__are_equal(const interfaces__action__BasicTask_GetResult_Request * lhs, const interfaces__action__BasicTask_GetResult_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__are_equal(
      &(lhs->goal_id), &(rhs->goal_id)))
  {
    return false;
  }
  return true;
}

bool
interfaces__action__BasicTask_GetResult_Request__copy(
  const interfaces__action__BasicTask_GetResult_Request * input,
  interfaces__action__BasicTask_GetResult_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__copy(
      &(input->goal_id), &(output->goal_id)))
  {
    return false;
  }
  return true;
}

interfaces__action__BasicTask_GetResult_Request *
interfaces__action__BasicTask_GetResult_Request__create()
{
  interfaces__action__BasicTask_GetResult_Request * msg = (interfaces__action__BasicTask_GetResult_Request *)malloc(sizeof(interfaces__action__BasicTask_GetResult_Request));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__action__BasicTask_GetResult_Request));
  bool success = interfaces__action__BasicTask_GetResult_Request__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interfaces__action__BasicTask_GetResult_Request__destroy(interfaces__action__BasicTask_GetResult_Request * msg)
{
  if (msg) {
    interfaces__action__BasicTask_GetResult_Request__fini(msg);
  }
  free(msg);
}


bool
interfaces__action__BasicTask_GetResult_Request__Sequence__init(interfaces__action__BasicTask_GetResult_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interfaces__action__BasicTask_GetResult_Request * data = NULL;
  if (size) {
    data = (interfaces__action__BasicTask_GetResult_Request *)calloc(size, sizeof(interfaces__action__BasicTask_GetResult_Request));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__action__BasicTask_GetResult_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__action__BasicTask_GetResult_Request__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
interfaces__action__BasicTask_GetResult_Request__Sequence__fini(interfaces__action__BasicTask_GetResult_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__action__BasicTask_GetResult_Request__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

interfaces__action__BasicTask_GetResult_Request__Sequence *
interfaces__action__BasicTask_GetResult_Request__Sequence__create(size_t size)
{
  interfaces__action__BasicTask_GetResult_Request__Sequence * array = (interfaces__action__BasicTask_GetResult_Request__Sequence *)malloc(sizeof(interfaces__action__BasicTask_GetResult_Request__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interfaces__action__BasicTask_GetResult_Request__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interfaces__action__BasicTask_GetResult_Request__Sequence__destroy(interfaces__action__BasicTask_GetResult_Request__Sequence * array)
{
  if (array) {
    interfaces__action__BasicTask_GetResult_Request__Sequence__fini(array);
  }
  free(array);
}

bool
interfaces__action__BasicTask_GetResult_Request__Sequence__are_equal(const interfaces__action__BasicTask_GetResult_Request__Sequence * lhs, const interfaces__action__BasicTask_GetResult_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!interfaces__action__BasicTask_GetResult_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
interfaces__action__BasicTask_GetResult_Request__Sequence__copy(
  const interfaces__action__BasicTask_GetResult_Request__Sequence * input,
  interfaces__action__BasicTask_GetResult_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(interfaces__action__BasicTask_GetResult_Request);
    interfaces__action__BasicTask_GetResult_Request * data =
      (interfaces__action__BasicTask_GetResult_Request *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!interfaces__action__BasicTask_GetResult_Request__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          interfaces__action__BasicTask_GetResult_Request__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!interfaces__action__BasicTask_GetResult_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `result`
// already included above
// #include "interfaces/action/detail/basic_task__functions.h"

bool
interfaces__action__BasicTask_GetResult_Response__init(interfaces__action__BasicTask_GetResult_Response * msg)
{
  if (!msg) {
    return false;
  }
  // status
  // result
  if (!interfaces__action__BasicTask_Result__init(&msg->result)) {
    interfaces__action__BasicTask_GetResult_Response__fini(msg);
    return false;
  }
  return true;
}

void
interfaces__action__BasicTask_GetResult_Response__fini(interfaces__action__BasicTask_GetResult_Response * msg)
{
  if (!msg) {
    return;
  }
  // status
  // result
  interfaces__action__BasicTask_Result__fini(&msg->result);
}

bool
interfaces__action__BasicTask_GetResult_Response__are_equal(const interfaces__action__BasicTask_GetResult_Response * lhs, const interfaces__action__BasicTask_GetResult_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // status
  if (lhs->status != rhs->status) {
    return false;
  }
  // result
  if (!interfaces__action__BasicTask_Result__are_equal(
      &(lhs->result), &(rhs->result)))
  {
    return false;
  }
  return true;
}

bool
interfaces__action__BasicTask_GetResult_Response__copy(
  const interfaces__action__BasicTask_GetResult_Response * input,
  interfaces__action__BasicTask_GetResult_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // status
  output->status = input->status;
  // result
  if (!interfaces__action__BasicTask_Result__copy(
      &(input->result), &(output->result)))
  {
    return false;
  }
  return true;
}

interfaces__action__BasicTask_GetResult_Response *
interfaces__action__BasicTask_GetResult_Response__create()
{
  interfaces__action__BasicTask_GetResult_Response * msg = (interfaces__action__BasicTask_GetResult_Response *)malloc(sizeof(interfaces__action__BasicTask_GetResult_Response));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__action__BasicTask_GetResult_Response));
  bool success = interfaces__action__BasicTask_GetResult_Response__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interfaces__action__BasicTask_GetResult_Response__destroy(interfaces__action__BasicTask_GetResult_Response * msg)
{
  if (msg) {
    interfaces__action__BasicTask_GetResult_Response__fini(msg);
  }
  free(msg);
}


bool
interfaces__action__BasicTask_GetResult_Response__Sequence__init(interfaces__action__BasicTask_GetResult_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interfaces__action__BasicTask_GetResult_Response * data = NULL;
  if (size) {
    data = (interfaces__action__BasicTask_GetResult_Response *)calloc(size, sizeof(interfaces__action__BasicTask_GetResult_Response));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__action__BasicTask_GetResult_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__action__BasicTask_GetResult_Response__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
interfaces__action__BasicTask_GetResult_Response__Sequence__fini(interfaces__action__BasicTask_GetResult_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__action__BasicTask_GetResult_Response__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

interfaces__action__BasicTask_GetResult_Response__Sequence *
interfaces__action__BasicTask_GetResult_Response__Sequence__create(size_t size)
{
  interfaces__action__BasicTask_GetResult_Response__Sequence * array = (interfaces__action__BasicTask_GetResult_Response__Sequence *)malloc(sizeof(interfaces__action__BasicTask_GetResult_Response__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interfaces__action__BasicTask_GetResult_Response__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interfaces__action__BasicTask_GetResult_Response__Sequence__destroy(interfaces__action__BasicTask_GetResult_Response__Sequence * array)
{
  if (array) {
    interfaces__action__BasicTask_GetResult_Response__Sequence__fini(array);
  }
  free(array);
}

bool
interfaces__action__BasicTask_GetResult_Response__Sequence__are_equal(const interfaces__action__BasicTask_GetResult_Response__Sequence * lhs, const interfaces__action__BasicTask_GetResult_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!interfaces__action__BasicTask_GetResult_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
interfaces__action__BasicTask_GetResult_Response__Sequence__copy(
  const interfaces__action__BasicTask_GetResult_Response__Sequence * input,
  interfaces__action__BasicTask_GetResult_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(interfaces__action__BasicTask_GetResult_Response);
    interfaces__action__BasicTask_GetResult_Response * data =
      (interfaces__action__BasicTask_GetResult_Response *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!interfaces__action__BasicTask_GetResult_Response__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          interfaces__action__BasicTask_GetResult_Response__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!interfaces__action__BasicTask_GetResult_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__functions.h"
// Member `feedback`
// already included above
// #include "interfaces/action/detail/basic_task__functions.h"

bool
interfaces__action__BasicTask_FeedbackMessage__init(interfaces__action__BasicTask_FeedbackMessage * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    interfaces__action__BasicTask_FeedbackMessage__fini(msg);
    return false;
  }
  // feedback
  if (!interfaces__action__BasicTask_Feedback__init(&msg->feedback)) {
    interfaces__action__BasicTask_FeedbackMessage__fini(msg);
    return false;
  }
  return true;
}

void
interfaces__action__BasicTask_FeedbackMessage__fini(interfaces__action__BasicTask_FeedbackMessage * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
  // feedback
  interfaces__action__BasicTask_Feedback__fini(&msg->feedback);
}

bool
interfaces__action__BasicTask_FeedbackMessage__are_equal(const interfaces__action__BasicTask_FeedbackMessage * lhs, const interfaces__action__BasicTask_FeedbackMessage * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__are_equal(
      &(lhs->goal_id), &(rhs->goal_id)))
  {
    return false;
  }
  // feedback
  if (!interfaces__action__BasicTask_Feedback__are_equal(
      &(lhs->feedback), &(rhs->feedback)))
  {
    return false;
  }
  return true;
}

bool
interfaces__action__BasicTask_FeedbackMessage__copy(
  const interfaces__action__BasicTask_FeedbackMessage * input,
  interfaces__action__BasicTask_FeedbackMessage * output)
{
  if (!input || !output) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__copy(
      &(input->goal_id), &(output->goal_id)))
  {
    return false;
  }
  // feedback
  if (!interfaces__action__BasicTask_Feedback__copy(
      &(input->feedback), &(output->feedback)))
  {
    return false;
  }
  return true;
}

interfaces__action__BasicTask_FeedbackMessage *
interfaces__action__BasicTask_FeedbackMessage__create()
{
  interfaces__action__BasicTask_FeedbackMessage * msg = (interfaces__action__BasicTask_FeedbackMessage *)malloc(sizeof(interfaces__action__BasicTask_FeedbackMessage));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__action__BasicTask_FeedbackMessage));
  bool success = interfaces__action__BasicTask_FeedbackMessage__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interfaces__action__BasicTask_FeedbackMessage__destroy(interfaces__action__BasicTask_FeedbackMessage * msg)
{
  if (msg) {
    interfaces__action__BasicTask_FeedbackMessage__fini(msg);
  }
  free(msg);
}


bool
interfaces__action__BasicTask_FeedbackMessage__Sequence__init(interfaces__action__BasicTask_FeedbackMessage__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interfaces__action__BasicTask_FeedbackMessage * data = NULL;
  if (size) {
    data = (interfaces__action__BasicTask_FeedbackMessage *)calloc(size, sizeof(interfaces__action__BasicTask_FeedbackMessage));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__action__BasicTask_FeedbackMessage__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__action__BasicTask_FeedbackMessage__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
interfaces__action__BasicTask_FeedbackMessage__Sequence__fini(interfaces__action__BasicTask_FeedbackMessage__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__action__BasicTask_FeedbackMessage__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

interfaces__action__BasicTask_FeedbackMessage__Sequence *
interfaces__action__BasicTask_FeedbackMessage__Sequence__create(size_t size)
{
  interfaces__action__BasicTask_FeedbackMessage__Sequence * array = (interfaces__action__BasicTask_FeedbackMessage__Sequence *)malloc(sizeof(interfaces__action__BasicTask_FeedbackMessage__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interfaces__action__BasicTask_FeedbackMessage__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interfaces__action__BasicTask_FeedbackMessage__Sequence__destroy(interfaces__action__BasicTask_FeedbackMessage__Sequence * array)
{
  if (array) {
    interfaces__action__BasicTask_FeedbackMessage__Sequence__fini(array);
  }
  free(array);
}

bool
interfaces__action__BasicTask_FeedbackMessage__Sequence__are_equal(const interfaces__action__BasicTask_FeedbackMessage__Sequence * lhs, const interfaces__action__BasicTask_FeedbackMessage__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!interfaces__action__BasicTask_FeedbackMessage__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
interfaces__action__BasicTask_FeedbackMessage__Sequence__copy(
  const interfaces__action__BasicTask_FeedbackMessage__Sequence * input,
  interfaces__action__BasicTask_FeedbackMessage__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(interfaces__action__BasicTask_FeedbackMessage);
    interfaces__action__BasicTask_FeedbackMessage * data =
      (interfaces__action__BasicTask_FeedbackMessage *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!interfaces__action__BasicTask_FeedbackMessage__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          interfaces__action__BasicTask_FeedbackMessage__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!interfaces__action__BasicTask_FeedbackMessage__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
