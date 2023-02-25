// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:msg/Manip.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__MANIP__TRAITS_HPP_
#define INTERFACES__MSG__DETAIL__MANIP__TRAITS_HPP_

#include "interfaces/msg/detail/manip__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const interfaces::msg::Manip & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: manip_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "manip_id: ";
    value_to_yaml(msg.manip_id, out);
    out << "\n";
  }

  // member: activated
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "activated: ";
    value_to_yaml(msg.activated, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const interfaces::msg::Manip & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<interfaces::msg::Manip>()
{
  return "interfaces::msg::Manip";
}

template<>
inline const char * name<interfaces::msg::Manip>()
{
  return "interfaces/msg/Manip";
}

template<>
struct has_fixed_size<interfaces::msg::Manip>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<interfaces::msg::Manip>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<interfaces::msg::Manip>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__MSG__DETAIL__MANIP__TRAITS_HPP_
