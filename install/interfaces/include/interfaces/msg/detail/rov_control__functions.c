// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from interfaces:msg/ROVControl.idl
// generated code does not contain a copyright notice
#include "interfaces/msg/detail/rov_control__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
interfaces__msg__ROVControl__init(interfaces__msg__ROVControl * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    interfaces__msg__ROVControl__fini(msg);
    return false;
  }
  // x
  msg->x = 1500;
  // y
  msg->y = 1500;
  // z
  msg->z = 1500;
  // yaw
  msg->yaw = 1500;
  // pitch
  msg->pitch = 1500;
  // roll
  msg->roll = 1500;
  return true;
}

void
interfaces__msg__ROVControl__fini(interfaces__msg__ROVControl * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // x
  // y
  // z
  // yaw
  // pitch
  // roll
}

bool
interfaces__msg__ROVControl__are_equal(const interfaces__msg__ROVControl * lhs, const interfaces__msg__ROVControl * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // x
  if (lhs->x != rhs->x) {
    return false;
  }
  // y
  if (lhs->y != rhs->y) {
    return false;
  }
  // z
  if (lhs->z != rhs->z) {
    return false;
  }
  // yaw
  if (lhs->yaw != rhs->yaw) {
    return false;
  }
  // pitch
  if (lhs->pitch != rhs->pitch) {
    return false;
  }
  // roll
  if (lhs->roll != rhs->roll) {
    return false;
  }
  return true;
}

bool
interfaces__msg__ROVControl__copy(
  const interfaces__msg__ROVControl * input,
  interfaces__msg__ROVControl * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // x
  output->x = input->x;
  // y
  output->y = input->y;
  // z
  output->z = input->z;
  // yaw
  output->yaw = input->yaw;
  // pitch
  output->pitch = input->pitch;
  // roll
  output->roll = input->roll;
  return true;
}

interfaces__msg__ROVControl *
interfaces__msg__ROVControl__create()
{
  interfaces__msg__ROVControl * msg = (interfaces__msg__ROVControl *)malloc(sizeof(interfaces__msg__ROVControl));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__msg__ROVControl));
  bool success = interfaces__msg__ROVControl__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interfaces__msg__ROVControl__destroy(interfaces__msg__ROVControl * msg)
{
  if (msg) {
    interfaces__msg__ROVControl__fini(msg);
  }
  free(msg);
}


bool
interfaces__msg__ROVControl__Sequence__init(interfaces__msg__ROVControl__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interfaces__msg__ROVControl * data = NULL;
  if (size) {
    data = (interfaces__msg__ROVControl *)calloc(size, sizeof(interfaces__msg__ROVControl));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__msg__ROVControl__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__msg__ROVControl__fini(&data[i - 1]);
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
interfaces__msg__ROVControl__Sequence__fini(interfaces__msg__ROVControl__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__msg__ROVControl__fini(&array->data[i]);
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

interfaces__msg__ROVControl__Sequence *
interfaces__msg__ROVControl__Sequence__create(size_t size)
{
  interfaces__msg__ROVControl__Sequence * array = (interfaces__msg__ROVControl__Sequence *)malloc(sizeof(interfaces__msg__ROVControl__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interfaces__msg__ROVControl__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interfaces__msg__ROVControl__Sequence__destroy(interfaces__msg__ROVControl__Sequence * array)
{
  if (array) {
    interfaces__msg__ROVControl__Sequence__fini(array);
  }
  free(array);
}

bool
interfaces__msg__ROVControl__Sequence__are_equal(const interfaces__msg__ROVControl__Sequence * lhs, const interfaces__msg__ROVControl__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!interfaces__msg__ROVControl__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
interfaces__msg__ROVControl__Sequence__copy(
  const interfaces__msg__ROVControl__Sequence * input,
  interfaces__msg__ROVControl__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(interfaces__msg__ROVControl);
    interfaces__msg__ROVControl * data =
      (interfaces__msg__ROVControl *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!interfaces__msg__ROVControl__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          interfaces__msg__ROVControl__fini(&data[i]);
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
    if (!interfaces__msg__ROVControl__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
