import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './OrderTable.css';

const OrderTable = () => {
    const [orders, setOrders] = useState([]);
    const [message, setMessage] = useState('');

    useEffect(() => {
        fetchOrders();
    }, []);

    const fetchOrders = async () => {
        try {
            const response = await axios.get('http://localhost:8000/api/orders/');
            setOrders(response.data);
        } catch (error) {
            console.error('Error fetching orders:', error);
        }
    };

    const deleteOrder = async (orderId, orderName, orderFirstName, orderPosition) => {
        try {
            await axios.delete(`http://localhost:8000/api/orders/${orderId}/`);
            setOrders(orders.filter(order => order.task_id !== orderId));
            const currentDateTime = new Date().toLocaleString();
            setMessage(`Task ${orderId} with name ${orderName} was processed by ${orderFirstName} ${orderPosition} in ${currentDateTime}`);
        } catch (error) {
            console.error('Error deleting order:', error);
        }
    };

    return (
        <div class="container">
            {message && <div class="alert-box success"><span>success: </span>{message}</div>}
            <table class="order-table">
                <thead>
                    <tr>
                        <th>Order</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {orders.map(order => (
                        <tr key={order.id}>
                            <td>{order.name}</td>
                            <td>
                                <button onClick={() => deleteOrder(order.task_id, order.name, order.employee.first_name,
                                order.employee.position)}>Delete</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default OrderTable;
