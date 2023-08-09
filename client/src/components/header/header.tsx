import Link from 'next/link';

import { navLinks } from './nav-links';
import { UserProps } from '@/app-types/user';

type HeaderProps = {
  currentUser: UserProps;
};

export default function Header({ currentUser }: HeaderProps) {
  return (
    <header>
      <nav
        className="navbar sticky-top navbar-expand-lg bg-dark"
        data-bs-theme="dark"
      >
        <div className="container-fluid">
          <Link href="/">
            <a className="navbar-brand">EventWise</a>
          </Link>
          <ul className="navbar-nav">
            {currentUser ? (
              <Link href="/auth/logout">
                <a className="nav-link">Log Out</a>
              </Link>
            ) : (
              navLinks.map((nv) => (
                <li className="nav-item" key={nv.name}>
                  <Link href={nv.href}>
                    <a className="nav-link">{nv.name}</a>
                  </Link>
                </li>
              ))
            )}
          </ul>
        </div>
      </nav>
    </header>
  );
}
