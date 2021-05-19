#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mi
Version  : 1.0
Release  : 35
URL      : https://cran.r-project.org/src/contrib/mi_1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mi_1.0.tar.gz
Summary  : Missing Data Imputation and Model Checking
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-arm
Requires: R-betareg
Requires: R-truncnorm
BuildRequires : R-arm
BuildRequires : R-betareg
BuildRequires : R-truncnorm
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n mi
cd %{_builddir}/mi

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589779992

%install
export SOURCE_DATE_EPOCH=1589779992
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mi
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mi
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mi
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc mi || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mi/CITATION
/usr/lib64/R/library/mi/DESCRIPTION
/usr/lib64/R/library/mi/INDEX
/usr/lib64/R/library/mi/Meta/Rd.rds
/usr/lib64/R/library/mi/Meta/data.rds
/usr/lib64/R/library/mi/Meta/features.rds
/usr/lib64/R/library/mi/Meta/hsearch.rds
/usr/lib64/R/library/mi/Meta/links.rds
/usr/lib64/R/library/mi/Meta/nsInfo.rds
/usr/lib64/R/library/mi/Meta/package.rds
/usr/lib64/R/library/mi/Meta/vignette.rds
/usr/lib64/R/library/mi/NAMESPACE
/usr/lib64/R/library/mi/R/mi
/usr/lib64/R/library/mi/R/mi.rdb
/usr/lib64/R/library/mi/R/mi.rdx
/usr/lib64/R/library/mi/R/sysdata.rdb
/usr/lib64/R/library/mi/R/sysdata.rdx
/usr/lib64/R/library/mi/data/CHAIN.RData
/usr/lib64/R/library/mi/data/nlsyV.RData
/usr/lib64/R/library/mi/doc/index.html
/usr/lib64/R/library/mi/doc/mi_vignette.R
/usr/lib64/R/library/mi/doc/mi_vignette.Rmd
/usr/lib64/R/library/mi/doc/mi_vignette.pdf
/usr/lib64/R/library/mi/help/AnIndex
/usr/lib64/R/library/mi/help/aliases.rds
/usr/lib64/R/library/mi/help/mi.rdb
/usr/lib64/R/library/mi/help/mi.rdx
/usr/lib64/R/library/mi/help/paths.rds
/usr/lib64/R/library/mi/html/00Index.html
/usr/lib64/R/library/mi/html/R.css
/usr/lib64/R/library/mi/tests/missing_data.frame.R
/usr/lib64/R/library/mi/tests/missing_variable.R
