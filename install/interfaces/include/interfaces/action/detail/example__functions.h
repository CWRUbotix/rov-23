// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from interfaces:action/Example.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__ACTION__DETAIL__EXAMPLE__FUNCTIONS_H_
#define INTERFACES__ACTION__DETAIL__EXAMPLE__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "interfaces/action/detail/example__struct.h"

/// Initialize action/Example message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * interfaces__action__Example_Goal
 * )) before or use
 * interfaces__action__Example_Goal__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_Goal__init(interfaces__action__Example_Goal * msg);

/// Finalize action/Example message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_Goal__fini(interfaces__action__Example_Goal * msg);

/// Create action/Example message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * interfaces__action__Example_Goal__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Example_Goal *
interfaces__action__Example_Goal__create();

/// Destroy action/Example message.
/**
 * It calls
 * interfaces__action__Example_Goal__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_Goal__destroy(interfaces__action__Example_Goal * msg);

/// Check for action/Example message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_Goal__are_equal(const interfaces__action__Example_Goal * lhs, const interfaces__action__Example_Goal * rhs);

/// Copy a action/Example message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_Goal__copy(
  const interfaces__action__Example_Goal * input,
  interfaces__action__Example_Goal * output);

/// Initialize array of action/Example messages.
/**
 * It allocates the memory for the number of elements and calls
 * interfaces__action__Example_Goal__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_Goal__Sequence__init(interfaces__action__Example_Goal__Sequence * array, size_t size);

/// Finalize array of action/Example messages.
/**
 * It calls
 * interfaces__action__Example_Goal__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_Goal__Sequence__fini(interfaces__action__Example_Goal__Sequence * array);

/// Create array of action/Example messages.
/**
 * It allocates the memory for the array and calls
 * interfaces__action__Example_Goal__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Example_Goal__Sequence *
interfaces__action__Example_Goal__Sequence__create(size_t size);

/// Destroy array of action/Example messages.
/**
 * It calls
 * interfaces__action__Example_Goal__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_Goal__Sequence__destroy(interfaces__action__Example_Goal__Sequence * array);

/// Check for action/Example message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_Goal__Sequence__are_equal(const interfaces__action__Example_Goal__Sequence * lhs, const interfaces__action__Example_Goal__Sequence * rhs);

/// Copy an array of action/Example messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_Goal__Sequence__copy(
  const interfaces__action__Example_Goal__Sequence * input,
  interfaces__action__Example_Goal__Sequence * output);

/// Initialize action/Example message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * interfaces__action__Example_Result
 * )) before or use
 * interfaces__action__Example_Result__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_Result__init(interfaces__action__Example_Result * msg);

/// Finalize action/Example message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_Result__fini(interfaces__action__Example_Result * msg);

/// Create action/Example message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * interfaces__action__Example_Result__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Example_Result *
interfaces__action__Example_Result__create();

/// Destroy action/Example message.
/**
 * It calls
 * interfaces__action__Example_Result__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_Result__destroy(interfaces__action__Example_Result * msg);

/// Check for action/Example message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_Result__are_equal(const interfaces__action__Example_Result * lhs, const interfaces__action__Example_Result * rhs);

/// Copy a action/Example message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_Result__copy(
  const interfaces__action__Example_Result * input,
  interfaces__action__Example_Result * output);

/// Initialize array of action/Example messages.
/**
 * It allocates the memory for the number of elements and calls
 * interfaces__action__Example_Result__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_Result__Sequence__init(interfaces__action__Example_Result__Sequence * array, size_t size);

/// Finalize array of action/Example messages.
/**
 * It calls
 * interfaces__action__Example_Result__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_Result__Sequence__fini(interfaces__action__Example_Result__Sequence * array);

/// Create array of action/Example messages.
/**
 * It allocates the memory for the array and calls
 * interfaces__action__Example_Result__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Example_Result__Sequence *
interfaces__action__Example_Result__Sequence__create(size_t size);

/// Destroy array of action/Example messages.
/**
 * It calls
 * interfaces__action__Example_Result__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_Result__Sequence__destroy(interfaces__action__Example_Result__Sequence * array);

/// Check for action/Example message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_Result__Sequence__are_equal(const interfaces__action__Example_Result__Sequence * lhs, const interfaces__action__Example_Result__Sequence * rhs);

/// Copy an array of action/Example messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_Result__Sequence__copy(
  const interfaces__action__Example_Result__Sequence * input,
  interfaces__action__Example_Result__Sequence * output);

/// Initialize action/Example message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * interfaces__action__Example_Feedback
 * )) before or use
 * interfaces__action__Example_Feedback__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_Feedback__init(interfaces__action__Example_Feedback * msg);

/// Finalize action/Example message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_Feedback__fini(interfaces__action__Example_Feedback * msg);

/// Create action/Example message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * interfaces__action__Example_Feedback__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Example_Feedback *
interfaces__action__Example_Feedback__create();

/// Destroy action/Example message.
/**
 * It calls
 * interfaces__action__Example_Feedback__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_Feedback__destroy(interfaces__action__Example_Feedback * msg);

/// Check for action/Example message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_Feedback__are_equal(const interfaces__action__Example_Feedback * lhs, const interfaces__action__Example_Feedback * rhs);

/// Copy a action/Example message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_Feedback__copy(
  const interfaces__action__Example_Feedback * input,
  interfaces__action__Example_Feedback * output);

/// Initialize array of action/Example messages.
/**
 * It allocates the memory for the number of elements and calls
 * interfaces__action__Example_Feedback__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_Feedback__Sequence__init(interfaces__action__Example_Feedback__Sequence * array, size_t size);

/// Finalize array of action/Example messages.
/**
 * It calls
 * interfaces__action__Example_Feedback__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_Feedback__Sequence__fini(interfaces__action__Example_Feedback__Sequence * array);

/// Create array of action/Example messages.
/**
 * It allocates the memory for the array and calls
 * interfaces__action__Example_Feedback__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Example_Feedback__Sequence *
interfaces__action__Example_Feedback__Sequence__create(size_t size);

/// Destroy array of action/Example messages.
/**
 * It calls
 * interfaces__action__Example_Feedback__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_Feedback__Sequence__destroy(interfaces__action__Example_Feedback__Sequence * array);

/// Check for action/Example message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_Feedback__Sequence__are_equal(const interfaces__action__Example_Feedback__Sequence * lhs, const interfaces__action__Example_Feedback__Sequence * rhs);

/// Copy an array of action/Example messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_Feedback__Sequence__copy(
  const interfaces__action__Example_Feedback__Sequence * input,
  interfaces__action__Example_Feedback__Sequence * output);

/// Initialize action/Example message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * interfaces__action__Example_SendGoal_Request
 * )) before or use
 * interfaces__action__Example_SendGoal_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_SendGoal_Request__init(interfaces__action__Example_SendGoal_Request * msg);

/// Finalize action/Example message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_SendGoal_Request__fini(interfaces__action__Example_SendGoal_Request * msg);

/// Create action/Example message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * interfaces__action__Example_SendGoal_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Example_SendGoal_Request *
interfaces__action__Example_SendGoal_Request__create();

/// Destroy action/Example message.
/**
 * It calls
 * interfaces__action__Example_SendGoal_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_SendGoal_Request__destroy(interfaces__action__Example_SendGoal_Request * msg);

/// Check for action/Example message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_SendGoal_Request__are_equal(const interfaces__action__Example_SendGoal_Request * lhs, const interfaces__action__Example_SendGoal_Request * rhs);

/// Copy a action/Example message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_SendGoal_Request__copy(
  const interfaces__action__Example_SendGoal_Request * input,
  interfaces__action__Example_SendGoal_Request * output);

/// Initialize array of action/Example messages.
/**
 * It allocates the memory for the number of elements and calls
 * interfaces__action__Example_SendGoal_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_SendGoal_Request__Sequence__init(interfaces__action__Example_SendGoal_Request__Sequence * array, size_t size);

/// Finalize array of action/Example messages.
/**
 * It calls
 * interfaces__action__Example_SendGoal_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_SendGoal_Request__Sequence__fini(interfaces__action__Example_SendGoal_Request__Sequence * array);

/// Create array of action/Example messages.
/**
 * It allocates the memory for the array and calls
 * interfaces__action__Example_SendGoal_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Example_SendGoal_Request__Sequence *
interfaces__action__Example_SendGoal_Request__Sequence__create(size_t size);

/// Destroy array of action/Example messages.
/**
 * It calls
 * interfaces__action__Example_SendGoal_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_SendGoal_Request__Sequence__destroy(interfaces__action__Example_SendGoal_Request__Sequence * array);

/// Check for action/Example message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_SendGoal_Request__Sequence__are_equal(const interfaces__action__Example_SendGoal_Request__Sequence * lhs, const interfaces__action__Example_SendGoal_Request__Sequence * rhs);

/// Copy an array of action/Example messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_SendGoal_Request__Sequence__copy(
  const interfaces__action__Example_SendGoal_Request__Sequence * input,
  interfaces__action__Example_SendGoal_Request__Sequence * output);

/// Initialize action/Example message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * interfaces__action__Example_SendGoal_Response
 * )) before or use
 * interfaces__action__Example_SendGoal_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_SendGoal_Response__init(interfaces__action__Example_SendGoal_Response * msg);

/// Finalize action/Example message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_SendGoal_Response__fini(interfaces__action__Example_SendGoal_Response * msg);

/// Create action/Example message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * interfaces__action__Example_SendGoal_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Example_SendGoal_Response *
interfaces__action__Example_SendGoal_Response__create();

/// Destroy action/Example message.
/**
 * It calls
 * interfaces__action__Example_SendGoal_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_SendGoal_Response__destroy(interfaces__action__Example_SendGoal_Response * msg);

/// Check for action/Example message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_SendGoal_Response__are_equal(const interfaces__action__Example_SendGoal_Response * lhs, const interfaces__action__Example_SendGoal_Response * rhs);

/// Copy a action/Example message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_SendGoal_Response__copy(
  const interfaces__action__Example_SendGoal_Response * input,
  interfaces__action__Example_SendGoal_Response * output);

/// Initialize array of action/Example messages.
/**
 * It allocates the memory for the number of elements and calls
 * interfaces__action__Example_SendGoal_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_SendGoal_Response__Sequence__init(interfaces__action__Example_SendGoal_Response__Sequence * array, size_t size);

/// Finalize array of action/Example messages.
/**
 * It calls
 * interfaces__action__Example_SendGoal_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_SendGoal_Response__Sequence__fini(interfaces__action__Example_SendGoal_Response__Sequence * array);

/// Create array of action/Example messages.
/**
 * It allocates the memory for the array and calls
 * interfaces__action__Example_SendGoal_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Example_SendGoal_Response__Sequence *
interfaces__action__Example_SendGoal_Response__Sequence__create(size_t size);

/// Destroy array of action/Example messages.
/**
 * It calls
 * interfaces__action__Example_SendGoal_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_SendGoal_Response__Sequence__destroy(interfaces__action__Example_SendGoal_Response__Sequence * array);

/// Check for action/Example message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_SendGoal_Response__Sequence__are_equal(const interfaces__action__Example_SendGoal_Response__Sequence * lhs, const interfaces__action__Example_SendGoal_Response__Sequence * rhs);

/// Copy an array of action/Example messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_SendGoal_Response__Sequence__copy(
  const interfaces__action__Example_SendGoal_Response__Sequence * input,
  interfaces__action__Example_SendGoal_Response__Sequence * output);

/// Initialize action/Example message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * interfaces__action__Example_GetResult_Request
 * )) before or use
 * interfaces__action__Example_GetResult_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_GetResult_Request__init(interfaces__action__Example_GetResult_Request * msg);

/// Finalize action/Example message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_GetResult_Request__fini(interfaces__action__Example_GetResult_Request * msg);

/// Create action/Example message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * interfaces__action__Example_GetResult_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Example_GetResult_Request *
interfaces__action__Example_GetResult_Request__create();

/// Destroy action/Example message.
/**
 * It calls
 * interfaces__action__Example_GetResult_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_GetResult_Request__destroy(interfaces__action__Example_GetResult_Request * msg);

/// Check for action/Example message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_GetResult_Request__are_equal(const interfaces__action__Example_GetResult_Request * lhs, const interfaces__action__Example_GetResult_Request * rhs);

/// Copy a action/Example message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_GetResult_Request__copy(
  const interfaces__action__Example_GetResult_Request * input,
  interfaces__action__Example_GetResult_Request * output);

/// Initialize array of action/Example messages.
/**
 * It allocates the memory for the number of elements and calls
 * interfaces__action__Example_GetResult_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_GetResult_Request__Sequence__init(interfaces__action__Example_GetResult_Request__Sequence * array, size_t size);

/// Finalize array of action/Example messages.
/**
 * It calls
 * interfaces__action__Example_GetResult_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_GetResult_Request__Sequence__fini(interfaces__action__Example_GetResult_Request__Sequence * array);

/// Create array of action/Example messages.
/**
 * It allocates the memory for the array and calls
 * interfaces__action__Example_GetResult_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Example_GetResult_Request__Sequence *
interfaces__action__Example_GetResult_Request__Sequence__create(size_t size);

/// Destroy array of action/Example messages.
/**
 * It calls
 * interfaces__action__Example_GetResult_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_GetResult_Request__Sequence__destroy(interfaces__action__Example_GetResult_Request__Sequence * array);

/// Check for action/Example message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_GetResult_Request__Sequence__are_equal(const interfaces__action__Example_GetResult_Request__Sequence * lhs, const interfaces__action__Example_GetResult_Request__Sequence * rhs);

/// Copy an array of action/Example messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_GetResult_Request__Sequence__copy(
  const interfaces__action__Example_GetResult_Request__Sequence * input,
  interfaces__action__Example_GetResult_Request__Sequence * output);

/// Initialize action/Example message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * interfaces__action__Example_GetResult_Response
 * )) before or use
 * interfaces__action__Example_GetResult_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_GetResult_Response__init(interfaces__action__Example_GetResult_Response * msg);

/// Finalize action/Example message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_GetResult_Response__fini(interfaces__action__Example_GetResult_Response * msg);

/// Create action/Example message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * interfaces__action__Example_GetResult_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Example_GetResult_Response *
interfaces__action__Example_GetResult_Response__create();

/// Destroy action/Example message.
/**
 * It calls
 * interfaces__action__Example_GetResult_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_GetResult_Response__destroy(interfaces__action__Example_GetResult_Response * msg);

/// Check for action/Example message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_GetResult_Response__are_equal(const interfaces__action__Example_GetResult_Response * lhs, const interfaces__action__Example_GetResult_Response * rhs);

/// Copy a action/Example message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_GetResult_Response__copy(
  const interfaces__action__Example_GetResult_Response * input,
  interfaces__action__Example_GetResult_Response * output);

/// Initialize array of action/Example messages.
/**
 * It allocates the memory for the number of elements and calls
 * interfaces__action__Example_GetResult_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_GetResult_Response__Sequence__init(interfaces__action__Example_GetResult_Response__Sequence * array, size_t size);

/// Finalize array of action/Example messages.
/**
 * It calls
 * interfaces__action__Example_GetResult_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_GetResult_Response__Sequence__fini(interfaces__action__Example_GetResult_Response__Sequence * array);

/// Create array of action/Example messages.
/**
 * It allocates the memory for the array and calls
 * interfaces__action__Example_GetResult_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Example_GetResult_Response__Sequence *
interfaces__action__Example_GetResult_Response__Sequence__create(size_t size);

/// Destroy array of action/Example messages.
/**
 * It calls
 * interfaces__action__Example_GetResult_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_GetResult_Response__Sequence__destroy(interfaces__action__Example_GetResult_Response__Sequence * array);

/// Check for action/Example message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_GetResult_Response__Sequence__are_equal(const interfaces__action__Example_GetResult_Response__Sequence * lhs, const interfaces__action__Example_GetResult_Response__Sequence * rhs);

/// Copy an array of action/Example messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_GetResult_Response__Sequence__copy(
  const interfaces__action__Example_GetResult_Response__Sequence * input,
  interfaces__action__Example_GetResult_Response__Sequence * output);

/// Initialize action/Example message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * interfaces__action__Example_FeedbackMessage
 * )) before or use
 * interfaces__action__Example_FeedbackMessage__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_FeedbackMessage__init(interfaces__action__Example_FeedbackMessage * msg);

/// Finalize action/Example message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_FeedbackMessage__fini(interfaces__action__Example_FeedbackMessage * msg);

/// Create action/Example message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * interfaces__action__Example_FeedbackMessage__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Example_FeedbackMessage *
interfaces__action__Example_FeedbackMessage__create();

/// Destroy action/Example message.
/**
 * It calls
 * interfaces__action__Example_FeedbackMessage__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_FeedbackMessage__destroy(interfaces__action__Example_FeedbackMessage * msg);

/// Check for action/Example message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_FeedbackMessage__are_equal(const interfaces__action__Example_FeedbackMessage * lhs, const interfaces__action__Example_FeedbackMessage * rhs);

/// Copy a action/Example message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_FeedbackMessage__copy(
  const interfaces__action__Example_FeedbackMessage * input,
  interfaces__action__Example_FeedbackMessage * output);

/// Initialize array of action/Example messages.
/**
 * It allocates the memory for the number of elements and calls
 * interfaces__action__Example_FeedbackMessage__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_FeedbackMessage__Sequence__init(interfaces__action__Example_FeedbackMessage__Sequence * array, size_t size);

/// Finalize array of action/Example messages.
/**
 * It calls
 * interfaces__action__Example_FeedbackMessage__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_FeedbackMessage__Sequence__fini(interfaces__action__Example_FeedbackMessage__Sequence * array);

/// Create array of action/Example messages.
/**
 * It allocates the memory for the array and calls
 * interfaces__action__Example_FeedbackMessage__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Example_FeedbackMessage__Sequence *
interfaces__action__Example_FeedbackMessage__Sequence__create(size_t size);

/// Destroy array of action/Example messages.
/**
 * It calls
 * interfaces__action__Example_FeedbackMessage__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Example_FeedbackMessage__Sequence__destroy(interfaces__action__Example_FeedbackMessage__Sequence * array);

/// Check for action/Example message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_FeedbackMessage__Sequence__are_equal(const interfaces__action__Example_FeedbackMessage__Sequence * lhs, const interfaces__action__Example_FeedbackMessage__Sequence * rhs);

/// Copy an array of action/Example messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Example_FeedbackMessage__Sequence__copy(
  const interfaces__action__Example_FeedbackMessage__Sequence * input,
  interfaces__action__Example_FeedbackMessage__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__ACTION__DETAIL__EXAMPLE__FUNCTIONS_H_
