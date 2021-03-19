import React from 'react'
import {NavLink} from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css';

export const Navbar = () => (
    <nav className="navbar navbar-dark navbar-expand-lg bg-primary">
        <div className="navbar-brand">
            Stonks
        </div>

        <ul className="navbar-nav">
            <li className="nav-item">
                <NavLink
                    className="nav-link"
                    to="/"
                    exact
                >
                    Главная
                </NavLink>
            </li>
            <li className="nav-item">
                <NavLink
                    className="nav-link"
                    to="/subs"
                >
                    Подписки
                </NavLink>
            </li>
            <li className="nav-item">
                <NavLink
                    className="nav-link"
                    to="/login"
                >
                    Вход
                </NavLink>
            </li>
            <li className="nav-item">
                <NavLink
                    className="nav-link"
                    to="/registration"
                >
                    Регистрация
                </NavLink>
            </li>
        </ul>
    </nav>
)