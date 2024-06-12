document.addEventListener("DOMContentLoaded", function() {
    const calendar = document.getElementById('calendar');
    const attendancePercentageElement = document.getElementById('attendance-percentage');
    const currentMonthElement = document.getElementById('current-month');
    const prevMonthButton = document.getElementById('prev-month');
    const nextMonthButton = document.getElementById('next-month');
    const date = new Date();
    const today = date.getDate();

    let totalSchoolDays = 0;
    let attendedDays = 0;

    // Define start and end dates for your semester
    const semesterStart = new Date('2024-04-10'); // Example: April 10, 2024
    const semesterEnd = new Date('2024-04-30');   // Example: April 30, 2024

    // Define holidays
    const holidays = [
        new Date('2024-04-14'), // Example: April 14, 2024
        new Date('2024-04-21')  // Example: April 21, 2024
    ];

    function createCalendar(year, month) {
        const daysInMonth = new Date(year, month + 1, 0).getDate();
        const startDay = new Date(year, month, 1).getDay();
        const endDay = new Date(year, month, daysInMonth).getDay();
        const calendarDays = [];

        // Only generate days for months within the semester range
        if (new Date(year, month, 1) <= semesterEnd && new Date(year, month, daysInMonth) >= semesterStart) {
            // Days of the month within the semester range
            for (let day = 1; day <= daysInMonth; day++) {
                const currentDay = new Date(year, month, day);
                const dayOfWeek = currentDay.getDay();
                // Count weekdays only within the semester and exclude holidays
                if (dayOfWeek !== 0 && dayOfWeek !== 6 && currentDay >= semesterStart && currentDay <= semesterEnd && !isHoliday(currentDay)) {
                    calendarDays.push(day);
                    totalSchoolDays++;
                }
            }
        }

        return calendarDays;
    }

    function renderCalendar(year, month) {
        currentMonthElement.textContent = `${getMonthName(month)} ${year}`;
        const days = createCalendar(year, month);
        calendar.innerHTML = '';
        const weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
        
        // Render weekdays header
        weekdays.forEach(day => {
            const dayElement = document.createElement('div');
            dayElement.classList.add('day', 'header');
            dayElement.textContent = day;
            calendar.appendChild(dayElement);
        });

        // Render days
        days.forEach((day, index) => {
            const dayElement = document.createElement('div');
            dayElement.classList.add('day');
            if (day === today) {
                dayElement.classList.add('today');
            }
            if (day) {
                dayElement.textContent = day;
                if (index % 7 === 0 || index % 7 === 6) {
                    dayElement.classList.add('weekend');
                } else {
                    dayElement.addEventListener('click', function() {
                        dayElement.classList.toggle('attended');
                        updateAttendance();
                    });
                }
            }
            calendar.appendChild(dayElement);
        });
    }

    function updateAttendance() {
        attendedDays = document.querySelectorAll('.day.attended').length;
        const attendancePercentage = totalSchoolDays ? ((attendedDays / totalSchoolDays) * 100).toFixed(2) : 0;
        attendancePercentageElement.textContent = `Attendance: ${attendancePercentage}%`;
    }

    function getMonthName(monthIndex) {
        const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
        return months[monthIndex];
    }

    // Function to check if a given date is a holiday
    function isHoliday(date) {
        console.log('Checking if', date.toDateString(), 'is a holiday');
        return holidays.some(holiday => holiday.getTime() === date.getTime());
    }

    prevMonthButton.addEventListener('click', function() {
        const currentMonth = new Date(currentMonthElement.textContent);
        const prevMonth = new Date(currentMonth.getFullYear(), currentMonth.getMonth() - 1, 1);
        renderCalendar(prevMonth.getFullYear(), prevMonth.getMonth());
    });

    nextMonthButton.addEventListener('click', function() {
        const currentMonth = new Date(currentMonthElement.textContent);
        const nextMonth = new Date(currentMonth.getFullYear(), currentMonth.getMonth() + 1, 1);
        renderCalendar(nextMonth.getFullYear(), nextMonth.getMonth());
    });

    const initialYear = date.getFullYear();
    const initialMonth = date.getMonth();
    renderCalendar(initialYear, initialMonth);
    updateAttendance();
});
