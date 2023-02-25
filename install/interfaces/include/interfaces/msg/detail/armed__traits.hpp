// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:msg/Armed.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__ARMED__TRAITS_HPP_
#define INTERFACES__MSG__DETAIL__ARMED__TRAITS_HPP_

#include "interfaces/msg/detail/armed__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const interfaces::msg::Armed & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: armed
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "armed: ";
    value_to_yaml(msg.armed, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const interfaces::msg::Armed & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<interfaces::msg::Armed>()
{
  return "interfaces::msg::Armed";
}

template<>
inline const char * name<interfaces::msg::Armed>()
{
  return "interfaces/msg/Armed";
}

template<>
struct has_fixed_size<interfaces::msg::Armed>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::msg::Armed>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interfaces::msg::Armed>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__MSG__DETAIL__ARMED__TRAITS_HPP_
