%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-elixir
Version:        0.6.1
Release:        5%{?dist}
Summary:        A declarative mapper for SQLAlchemy

Group:          Development/Languages
License:        MIT
URL:            http://elixir.ematia.de/
Source0:        http://pypi.python.org/packages/source/E/Elixir/Elixir-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel, python-setuptools, python-sqlalchemy, python-crypto, python-nose

Requires:       python-sqlalchemy, python-crypto


%description
Elixir is a declarative layer on top of SQLAlchemy. It is a fairly thin
wrapper, which provides the ability to define model objects following the
Active Record design pattern, and using a DSL syntax similar to that of the
Ruby on Rails ActiveRecord system.

Elixir does not intend to replace SQLAlchemy's core features, but instead
focuses on providing a simpler syntax for defining model objects when you do
not need the full expressiveness of SQLAlchemy's manual mapper definitions.


%prep
%setup -q -n Elixir-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
rm -rf build/lib/{tests,examples}/
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%check
%{__python} setup.py test

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE README TODO
# For noarch packages: sitelib
%{python_sitelib}/*


%changelog
* Fri Apr 23 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.6.1-5
- Added missing python-crypto to Requires
- Added test-suite execution with BuildRequires updated

* Thu Apr 22 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.6.1-4.2
- Fixed Source0 URL

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.6.1-4.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.6.1-2
- Rebuild for Python 2.6

* Wed Sep 17 2008 James Bowes <jbowes@redhat.com> 0.6.1-1
- Update to 0.6.1

* Thu Jul 24 2008 James Bowes <jbowes@redhat.com> 0.6.0-1
- Update to 0.6.0

* Sat Apr 05 2008 James Bowes <jbowes@redhat.com> 0.5.2-1
- Update to 0.5.2

* Mon Feb 11 2008 James Bowes <jbowes@redhat.com> 0.5.1-1
- Update to 0.5.1

* Thu Dec 13 2007 James Bowes <jbowes@redhat.com> - 0.5.0-1
- Update to 0.5.0

* Wed Nov 14 2007 Steve 'Ashcrow' Milner <me@stevemilner.org> - 0.4.0-1
- Updated for upstream 0.4.0.

* Sun Jun 24 2007 James Bowes <jbowes@redhat.com> - 0.3.0-1
- Initial packaging for Fedora.
