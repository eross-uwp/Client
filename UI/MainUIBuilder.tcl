#############################################################################
# Generated by PAGE version 4.24.1
#  in conjunction with Tcl version 8.6
#  Jul 16, 2019 04:06:17 PM CDT  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}



if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}


proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m48" -background {#d9d9d9} 
    wm focusmodel $top passive
    wm geometry $top 855x616+417+117
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 3204 881
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    button $top.but43 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Predict 
    vTcl:DefineAlias "$top.but43" "predict_btn" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.m48
    menu $site_3_0 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -font TkMenuFont -foreground {#000000} \
        -tearoff 0 
    ttk::entry $top.tEn52 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$top.tEn52" "TEntry1" vTcl:WidgetProc "Toplevel1" 1
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $top.scr58 \
        -background {#d9d9d9} -height 375 -highlightbackground {#d9d9d9} \
        -highlightcolor black -width 261 
    vTcl:DefineAlias "$top.scr58" "Scrolledlistbox1" vTcl:WidgetProc "Toplevel1" 1

    $top.scr58.01 configure -background white \
        -disabledforeground #a3a3a3 \
        -font TkFixedFont \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor #d9d9d9 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10
    ttk::label $top.tLa60 \
        -background {#d9d9d9} -foreground {#000000} -font TkDefaultFont \
        -relief flat -text {Course List} 
    vTcl:DefineAlias "$top.tLa60" "TLabel1" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $top.tLa61 \
        -background {#d9d9d9} -foreground {#000000} -font TkDefaultFont \
        -relief flat -text {Prerequisite Classes} 
    vTcl:DefineAlias "$top.tLa61" "TLabel2" vTcl:WidgetProc "Toplevel1" 1
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $top.scr62 \
        -background {#d9d9d9} -height 375 -highlightbackground {#d9d9d9} \
        -highlightcolor black -width 221 
    vTcl:DefineAlias "$top.scr62" "Scrolledlistbox1_2" vTcl:WidgetProc "Toplevel1" 1

    $top.scr62.01 configure -background white \
        -disabledforeground #a3a3a3 \
        -font TkFixedFont \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor #d9d9d9 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10
    ttk::label $top.tLa63 \
        -background {#d9d9d9} -foreground {#000000} -font TkDefaultFont \
        -relief flat -text Grade 
    vTcl:DefineAlias "$top.tLa63" "TLabel3" vTcl:WidgetProc "Toplevel1" 1
    vTcl::widgets::ttk::scrolledtext::CreateCmd $top.scr64 \
        -background {#d9d9d9} -height 201 -highlightbackground {#d9d9d9} \
        -highlightcolor black -width 201 
    vTcl:DefineAlias "$top.scr64" "Scrolledtext1" vTcl:WidgetProc "Toplevel1" 1

    $top.scr64.01 configure -background white \
        -font TkTextFont \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor black \
        -insertbackground black \
        -insertborderwidth 3 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10 \
        -wrap none
    button $top.but65 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Add 
    vTcl:DefineAlias "$top.but65" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but66 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Remove 
    vTcl:DefineAlias "$top.but66" "Button2" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but43 \
        -in $top -x 510 -y 530 -anchor nw -bordermode ignore 
    place $top.tEn52 \
        -in $top -x 640 -y 80 -anchor nw -bordermode ignore 
    place $top.scr58 \
        -in $top -x 20 -y 70 -width 261 -relwidth 0 -height 375 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa60 \
        -in $top -x 80 -y 40 -anchor nw -bordermode ignore 
    place $top.tLa61 \
        -in $top -x 430 -y 40 -anchor nw -bordermode ignore 
    place $top.scr62 \
        -in $top -x 370 -y 70 -width 221 -relwidth 0 -height 375 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa63 \
        -in $top -x 690 -y 40 -anchor nw -bordermode ignore 
    place $top.scr64 \
        -in $top -x 640 -y 360 -width 201 -relwidth 0 -height 201 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.but65 \
        -in $top -x 280 -y 180 -anchor nw -bordermode ignore 
    place $top.but66 \
        -in $top -x 320 -y 320 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

