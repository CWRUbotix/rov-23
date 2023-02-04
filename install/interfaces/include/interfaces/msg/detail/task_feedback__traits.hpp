// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:msg/TaskFeedback.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__TASK_FEEDBACK__TRAITS_HPP_
#define INTERFACES__MSG__DETAIL__TASK_FEEDBACK__TRAITS_HPP_

#include "interfaces/msg/detail/task_feedback__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const interfaces::msg::TaskFeedback & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: task_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "task_id: ";
    value_to_yaml(msg.task_id, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const interfaces::msg::TaskFeedback & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<interfaces::msg::TaskFeedback>()
{
  return "interfaces::msg::TaskFeedback";
}

template<>
inline const char * name<interfaces::msg::TaskFeedback>()
{
  return "interfaces/msg/TaskFeedback";
}

template<>
struct has_fixed_size<interfaces::msg::TaskFeedback>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::msg::TaskFeedback>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interfaces::msg::TaskFeedback>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__MSG__DETAIL__TASK_FEEDBACK__TRAITS_HPP_
