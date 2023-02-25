// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from interfaces:msg/Armed.idl
// generated code does not contain a copyright notice
#include "interfaces/msg/detail/armed__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


bool
interfaces__msg__Armed__init(interfaces__msg__Armed * msg)
{
  if (!msg) {
    return false;
  }
  // armed
  msg->armed = false;
  return true;
}

void
interfaces__msg__Armed__fini(interfaces__msg__Armed * msg)
{
  if (!msg) {
    return;
  }
  // armed
}

bool
interfaces__msg__Armed__are_equal(const interfaces__msg__Armed * lhs, const interfaces__msg__Armed * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // armed
  if (lhs->armed != rhs->armed) {
    return false;
  }
  return true;
}

bool
interfaces__msg__Armed__copy(
  const interfaces__msg__Armed * input,
  interfaces__msg__Armed * output)
{
  if (!input || !output) {
    return false;
  }
  // armed
  output->armed = input->armed;
  return true;
}

interfaces__msg__Armed *
interfaces__msg__Armed__create()
{
  interfaces__msg__Armed * msg = (interfaces__msg__Armed *)malloc(sizeof(interfaces__msg__Armed));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__msg__Armed));
  bool success = interfaces__msg__Armed__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interfaces__msg__Armed__destroy(interfaces__msg__Armed * msg)
{
  if (msg) {
    interfaces__msg__Armed__fini(msg);
  }
  free(msg);
}


bool
interfaces__msg__Armed__Sequence__init(interfaces__msg__Armed__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interfaces__msg__Armed * data = NULL;
  if (size) {
    data = (interfaces__msg__Armed *)calloc(size, sizeof(interfaces__msg__Armed));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__msg__Armed__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__msg__Armed__fini(&data[i - 1]);
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
interfaces__msg__Armed__Sequence__fini(interfaces__msg__Armed__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__msg__Armed__fini(&array->data[i]);
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

interfaces__msg__Armed__Sequence *
interfaces__msg__Armed__Sequence__create(size_t size)
{
  interfaces__msg__Armed__Sequence * array = (interfaces__msg__Armed__Sequence *)malloc(sizeof(interfaces__msg__Armed__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interfaces__msg__Armed__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interfaces__msg__Armed__Sequence__destroy(interfaces__msg__Armed__Sequence * array)
{
  if (array) {
    interfaces__msg__Armed__Sequence__fini(array);
  }
  free(array);
}

bool
interfaces__msg__Armed__Sequence__are_equal(const interfaces__msg__Armed__Sequence * lhs, const interfaces__msg__Armed__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!interfaces__msg__Armed__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
interfaces__msg__Armed__Sequence__copy(
  const interfaces__msg__Armed__Sequence * input,
  interfaces__msg__Armed__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(interfaces__msg__Armed);
    interfaces__msg__Armed * data =
      (interfaces__msg__Armed *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!interfaces__msg__Armed__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          interfaces__msg__Armed__fini(&data[i]);
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
    if (!interfaces__msg__Armed__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
