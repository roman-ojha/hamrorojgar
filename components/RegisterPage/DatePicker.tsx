import React, { useEffect, useState } from "react";
import styles from "@/styles/pages/register.module.scss";
import { UseFormRegister } from "react-hook-form";
import { CitizenForm } from "@/pages/register";
// import countDaysInMonth from "count-days-in-month";

interface DatePickerProps {
  register: UseFormRegister<CitizenForm>;
}

const DatePicker: React.FC<DatePickerProps> = ({
  register,
}): React.JSX.Element => {
  //   const [date, setDate] = useState({
  //     year: 0,
  //     month: 0,
  //     noOfDays: 0,
  //   });

  const currentDate = new Date().getFullYear(); // Try to implement this on backend

  return (
    <>
      <div className={styles.register__form__second_row__column__dob}>
        <label htmlFor="date-of-birth" data-field="date-of-birth">
          Date of birth
        </label>
        <div className={styles.register__form__second_row__column__dob__fields}>
          <select
            className={
              styles.register__form__second_row__column__dob__fields__select
            }
            id="dob-year"
            {...register("date_of_birth.year")}
            onChange={(e) => {
              //   setDate({
              //     ...date,
              //     year: parseInt(e.target.value),
              //     noOfDays:
              //       date.month != 0 ? countDaysInMonth(date.year, date.month) : 0,
              //   });
            }}
          >
            <option value="">Year</option>
            {Array.from({ length: 100 }).map((_, index) => (
              <option key={index} value={currentDate - index}>
                {currentDate - index}
              </option>
            ))}
          </select>
          <select
            className={
              styles.register__form__second_row__column__dob__fields__select
            }
            id="dob-month"
            {...register("date_of_birth.month")}
            // onChange={(e) => {
            //   setDate({
            //     ...date,
            //     month: parseInt(e.target.value),
            //     noOfDays:
            //       date.year != 0 ? countDaysInMonth(date.year, date.month) : 0,
            //   });
            // }}
          >
            <option value="">Month</option>
            <option value="01">Jan</option>
            <option value="02">Feb</option>
            <option value="03">Mars</option>
            <option value="04">April</option>
            <option value="05">May</option>
            <option value="06">June</option>
            <option value="07">July</option>
            <option value="08">August</option>
            <option value="09">Sep</option>
            <option value="10">Oct</option>
            <option value="11">Nov</option>
            <option value="12">Dec</option>
          </select>
          <select
            className={
              styles.register__form__second_row__column__dob__fields__select
            }
            id="dob-month"
            {...register("date_of_birth.day")}
          >
            <option value="">Day</option>
            {Array.from({ length: 31 }).map((_, index) => (
              <option key={index} value={index + 1}>
                {index + 1}
              </option>
            ))}
          </select>
        </div>
      </div>
    </>
  );
};

export default DatePicker;
