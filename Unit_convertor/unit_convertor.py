import streamlit as st

st.title("** Unit Convertor 🔄**")
print()

Available_conversions = [
                          (1, "°C", "°F"),
                          (2, "°F", "°C"),
                          (3, "km", "mi"),
                          (4, "mi", "km"),
                          (5, "kg", "lbs"),
                          (6, "lbs", "kg"),
                          (7, "L", "mL"),
                          (8, "mL", "L"),
                          (9, "cm", "ft"),
                          (10, "ft", "cm"),
                          (11, "m²", "ft²"),
                          (12, "ft²", "m²")
                        ]

st.header("Conversions Available: 🌍")
print()

with st.expander("Click here to see the available conversions 📜", expanded=True):
    for unit_num, from_unit, to_unit in Available_conversions:
        st.write(f"{unit_num}) {from_unit} ➡️ {to_unit}")

    print()

user_conversion = st.text_input("Enter the number of conversion you want to use (ex: num 1, 2, 3 ... etc) --->")

if user_conversion.strip().isdigit():
    conversion = int(user_conversion) -1
    if conversion < 0 or conversion > len(Available_conversions):
        st.error("❌ Invalid conversion number. Please enter a valid number.")
    else:
        unit_num, from_unit, to_unit = Available_conversions[conversion]
        print()
        from_value = st.text_input(f'enter {from_unit} ➡️ ')
        print()

        if from_value.strip():
            try:

                from_value = float(from_value)

                with st.container(border=True):

                    if unit_num == 1:  # Celsius to Fahrenheit
                        to_value = (from_value * 1.8) + 32
                        st.write("Answer: ✅")
                        st.subheader(f'{from_value} {from_unit} ➡️ {to_value} {to_unit}')
                    elif unit_num == 2:  # Fahrenheit to Celsius
                        to_value = (from_value - 32) / 1.8
                        st.write("Answer: ✅")
                        st.subheader(f'{from_value} {from_unit} ➡️ {to_value} {to_unit}')
                    elif unit_num == 3:  # Kilometers to Miles
                        to_value = from_value * 0.621371
                        st.write("Answer: ✅")
                        st.subheader(f'{from_value} {from_unit} ➡️ {to_value} {to_unit}')
                    elif unit_num == 4:  # Miles to Kilometers
                        to_value = from_value / 0.621371
                        st.write("Answer: ✅")
                        st.subheader(f'{from_value} {from_unit} ➡️ {to_value} {to_unit}')
                    elif unit_num == 5:  # Kilograms to Pounds
                        to_value = from_value * 2.20462
                        st.write("Answer: ✅")
                        st.subheader(f'{from_value} {from_unit} ➡️ {to_value} {to_unit}')
                    elif unit_num == 6:  # Pounds to Kilograms
                        to_value = from_value / 2.20462
                        st.write("Answer: ✅")
                        st.subheader(f'{from_value} {from_unit} ➡️ {to_value} {to_unit}')
                    elif unit_num == 7:  # Liters to Milliliters
                        to_value = from_value * 1000
                        st.write("Answer: ✅")
                        st.subheader(f'{from_value} {from_unit} ➡️ {to_value} {to_unit}')
                    elif unit_num == 8:  # Milliliters to Liters
                        to_value = from_value / 1000
                        st.write("Answer: ✅")
                        st.subheader(f'{from_value} {from_unit} ➡️ {to_value} {to_unit}')
                    elif unit_num == 9:  # Meters to Feet
                        to_value = from_value * 3.28084
                        st.write("Answer: ✅")
                        st.subheader(f'{from_value} {from_unit} ➡️ {to_value} {to_unit}')
                    elif unit_num == 10:  # Feet to Meters
                        to_value = from_value / 3.28084
                        st.write("Answer: ✅")
                        st.subheader(f'{from_value} {from_unit} ➡️ {to_value} {to_unit}')
                    elif unit_num == 19:  # Square Meters to Square Feet
                        to_value = from_value * 10.7639
                        st.write("Answer: ✅")
                        st.subheader(f'{from_value} {from_unit} ➡️ {to_value} {to_unit}')
                    elif unit_num == 20:  # Square Feet to Square Meters
                        to_value = from_value / 10.7639
                        st.write("Answer: ✅")
                        st.subheader(f'{from_value} {from_unit} ➡️ {to_value} {to_unit}')

            except:
                st.error("❌ Invalid input. Please enter a valid number.")
        else:
            st.warning("⚠️ Please enter a value to convert.")