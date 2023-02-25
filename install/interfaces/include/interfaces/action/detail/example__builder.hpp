// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:action/Example.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__ACTION__DETAIL__EXAMPLE__BUILDER_HPP_
#define INTERFACES__ACTION__DETAIL__EXAMPLE__BUILDER_HPP_

#include "interfaces/action/detail/example__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace interfaces
{

namespace action
{

namespace builder
{

class Init_Example_Goal_cheery
{
public:
  explicit Init_Example_Goal_cheery(::interfaces::action::Example_Goal & msg)
  : msg_(msg)
  {}
  ::interfaces::action::Example_Goal cheery(::interfaces::action::Example_Goal::_cheery_type arg)
  {
    msg_.cheery = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::action::Example_Goal msg_;
};

class Init_Example_Goal_morning
{
public:
  Init_Example_Goal_morning()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Example_Goal_cheery morning(::interfaces::action::Example_Goal::_morning_type arg)
  {
    msg_.morning = std::move(arg);
    return Init_Example_Goal_cheery(msg_);
  }

private:
  ::interfaces::action::Example_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::action::Example_Goal>()
{
  return interfaces::action::builder::Init_Example_Goal_morning();
}

}  // namespace interfaces


namespace interfaces
{

namespace action
{

namespace builder
{

class Init_Example_Result_message
{
public:
  Init_Example_Result_message()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::action::Example_Result message(::interfaces::action::Example_Result::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::action::Example_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::action::Example_Result>()
{
  return interfaces::action::builder::Init_Example_Result_message();
}

}  // namespace interfaces


namespace interfaces
{

namespace action
{

namespace builder
{

class Init_Example_Feedback_feedback_message
{
public:
  Init_Example_Feedback_feedback_message()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::action::Example_Feedback feedback_message(::interfaces::action::Example_Feedback::_feedback_message_type arg)
  {
    msg_.feedback_message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::action::Example_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::action::Example_Feedback>()
{
  return interfaces::action::builder::Init_Example_Feedback_feedback_message();
}

}  // namespace interfaces


namespace interfaces
{

namespace action
{

namespace builder
{

class Init_Example_SendGoal_Request_goal
{
public:
  explicit Init_Example_SendGoal_Request_goal(::interfaces::action::Example_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::interfaces::action::Example_SendGoal_Request goal(::interfaces::action::Example_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::action::Example_SendGoal_Request msg_;
};

class Init_Example_SendGoal_Request_goal_id
{
public:
  Init_Example_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Example_SendGoal_Request_goal goal_id(::interfaces::action::Example_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_Example_SendGoal_Request_goal(msg_);
  }

private:
  ::interfaces::action::Example_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::action::Example_SendGoal_Request>()
{
  return interfaces::action::builder::Init_Example_SendGoal_Request_goal_id();
}

}  // namespace interfaces


namespace interfaces
{

namespace action
{

namespace builder
{

class Init_Example_SendGoal_Response_stamp
{
public:
  explicit Init_Example_SendGoal_Response_stamp(::interfaces::action::Example_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::interfaces::action::Example_SendGoal_Response stamp(::interfaces::action::Example_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::action::Example_SendGoal_Response msg_;
};

class Init_Example_SendGoal_Response_accepted
{
public:
  Init_Example_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Example_SendGoal_Response_stamp accepted(::interfaces::action::Example_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_Example_SendGoal_Response_stamp(msg_);
  }

private:
  ::interfaces::action::Example_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::action::Example_SendGoal_Response>()
{
  return interfaces::action::builder::Init_Example_SendGoal_Response_accepted();
}

}  // namespace interfaces


namespace interfaces
{

namespace action
{

namespace builder
{

class Init_Example_GetResult_Request_goal_id
{
public:
  Init_Example_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::action::Example_GetResult_Request goal_id(::interfaces::action::Example_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::action::Example_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::action::Example_GetResult_Request>()
{
  return interfaces::action::builder::Init_Example_GetResult_Request_goal_id();
}

}  // namespace interfaces


namespace interfaces
{

namespace action
{

namespace builder
{

class Init_Example_GetResult_Response_result
{
public:
  explicit Init_Example_GetResult_Response_result(::interfaces::action::Example_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::interfaces::action::Example_GetResult_Response result(::interfaces::action::Example_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::action::Example_GetResult_Response msg_;
};

class Init_Example_GetResult_Response_status
{
public:
  Init_Example_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Example_GetResult_Response_result status(::interfaces::action::Example_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_Example_GetResult_Response_result(msg_);
  }

private:
  ::interfaces::action::Example_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::action::Example_GetResult_Response>()
{
  return interfaces::action::builder::Init_Example_GetResult_Response_status();
}

}  // namespace interfaces


namespace interfaces
{

namespace action
{

namespace builder
{

class Init_Example_FeedbackMessage_feedback
{
public:
  explicit Init_Example_FeedbackMessage_feedback(::interfaces::action::Example_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::interfaces::action::Example_FeedbackMessage feedback(::interfaces::action::Example_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::action::Example_FeedbackMessage msg_;
};

class Init_Example_FeedbackMessage_goal_id
{
public:
  Init_Example_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Example_FeedbackMessage_feedback goal_id(::interfaces::action::Example_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_Example_FeedbackMessage_feedback(msg_);
  }

private:
  ::interfaces::action::Example_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::action::Example_FeedbackMessage>()
{
  return interfaces::action::builder::Init_Example_FeedbackMessage_goal_id();
}

}  // namespace interfaces

#endif  // INTERFACES__ACTION__DETAIL__EXAMPLE__BUILDER_HPP_
