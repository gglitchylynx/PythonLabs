function addWorkplace(event) {
    event.preventDefault();
    
    const company = document.getElementById('company').value;
    const term = document.getElementById('term').value;
    
    fetch('/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            company: company,
            term: parseInt(term)
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById('total-term').textContent = data.total_term;

            const listElement = document.getElementById('workplaces-list');
            if (listElement) {
                listElement.innerHTML = '';
                data.workplaces.forEach(work => {
                    const li = document.createElement('li');
                    li.innerHTML = `
                        <span class="company">${work.company}</span>
                        <span class="term">${work.term} мес.</span>
                    `;
                    listElement.appendChild(li);
                });
            } else {
                const workplacesDiv = document.querySelector('.workplaces-list');
                workplacesDiv.innerHTML = `
                    <h3>Места работы:</h3>
                    <ul id="workplaces-list">
                        ${data.workplaces.map(work => `
                            <li>
                                <span class="company">${work.company}</span>
                                <span class="term">${work.term} мес.</span>
                            </li>
                        `).join('')}
                    </ul>
                `;
            }

            document.getElementById('workForm').reset();
        }
    })
    .catch(error => console.error('Error:', error));
}

function clearAll() {
    if (confirm('Вы уверены, что хотите очистить весь список?')) {
        fetch('/clear', {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById('total-term').textContent = data.total_term;

                const listElement = document.getElementById('workplaces-list');
                if (listElement) {
                    const workplacesDiv = document.querySelector('.workplaces-list');
                    workplacesDiv.innerHTML = `
                        <h3>Места работы:</h3>
                        <p class="empty-message">Пока нет записей о работе. Добавьте ваше первое место работы!</p>
                    `;
                }

                document.getElementById('workForm').reset();
            }
        })
        .catch(error => console.error('Error:', error));
    }
}