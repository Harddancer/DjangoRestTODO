import React from 'react'
const PROJECT = ({project}) => {
return (
<tr>
<td>
{project.name}
</td>
<td>
{project.users}
</td>

</tr>
)
}


const TODO = ({TODO}) => {
    return (
    <table>
    <th>
        name
    </th>
    <th>
    text
    </th>
    <th>
    date creation
    </th>
    <th>
    date update
    </th>
    <th>
    user
    </th>
    <th>
    status
    </th>
    {project.map((name) => <PROJECT name={name} />)}
    </table>
    )
    }
    export default TODO