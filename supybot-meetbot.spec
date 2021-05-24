Name:           supybot-meetbot
Version:        0.2
Release:        1%{?dist}
Summary:        Plugin for Supybot for handling IRC meetings

Group:          Applications/Internet
License:        BSD
URL:            https://github.com/fedora-infra/supybot-koji
Source0:        https://github.com/fedora-infra/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

Requires:       limnoria
Requires:       python3-pygments
Requires:       python3-docutils
Requires:       python3-kitchen

BuildArch:      noarch
BuildRequires:  python3-devel

%description
MeatBot is designed to assist in running meetings, taking notes, and so on. 
It is in pure python, as a plugin to supybot. However, there is a clear 
distinction between meeting-code and IRC-code, so it should be relatively 
easy to port to other bots. It is under the supybot license (3-clause BSD).

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT/%{python3_sitelib}/supybot/plugins/MeetBot
install -pm 644 supybot_meetbot/*.py $RPM_BUILD_ROOT/%{python3_sitelib}/supybot/plugins/MeetBot
install -pm 644 supybot_meetbot/*.css $RPM_BUILD_ROOT/%{python3_sitelib}/supybot/plugins/MeetBot

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.md supybot_meetbot/doc/Manual.txt supybot_meetbot/doc/meetingLocalConfig-example.py
%{python3_sitelib}/supybot/plugins/MeetBot

%changelog
* Mon May 24 2021 Ryan Lerch <rlerch@redhat.com> - 0.2-1
- Change to Python 3
- New 0.2 Release

* Wed Nov 18 2015 Kevin Fenzi <kevin@scrye.com> - 0.1.4-15
- Add patch to force meeting name on start. Fixes bug #1283357

* Sun Jan 05 2014 Kevin Fenzi <kevin@scrye.com> 0.1.4-12
- Add patch from Michael Scherer to show what undo undid. 

* Wed May 15 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.1.4-10
- Fix for traceback if meeting names contain non-ascii chars

* Fri Sep 11 2009 Kevin Fenzi <kevin@tummy.com> - 0.1.4-1
- Update to 0.1.4 release. 