import '/backend/api_requests/api_calls.dart';
import '/flutter_flow/flutter_flow_animations.dart';
import '/flutter_flow/flutter_flow_icon_button.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/flutter_flow/flutter_flow_widgets.dart';
import '/flutter_flow/permissions_util.dart';
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';
import 'package:record/record.dart';
import 'home_model.dart';
export 'home_model.dart';

class HomeWidget extends StatefulWidget {
  const HomeWidget({
    Key? key,
    String? userName,
  })  : this.userName = userName ?? '',
        super(key: key);

  final String userName;

  @override
  _HomeWidgetState createState() => _HomeWidgetState();
}

class _HomeWidgetState extends State<HomeWidget> with TickerProviderStateMixin {
  late HomeModel _model;

  final scaffoldKey = GlobalKey<ScaffoldState>();

  final animationsMap = {
    'iconButtonOnActionTriggerAnimation': AnimationInfo(
      trigger: AnimationTrigger.onActionTrigger,
      applyInitialState: true,
      effects: [
        ScaleEffect(
          curve: Curves.easeInOut,
          delay: 0.ms,
          duration: 2000.ms,
          begin: Offset(1.0, 1.0),
          end: Offset(1.5, 1.5),
        ),
      ],
    ),
  };

  @override
  void initState() {
    super.initState();
    _model = createModel(context, () => HomeModel());

    setupAnimations(
      animationsMap.values.where((anim) =>
          anim.trigger == AnimationTrigger.onActionTrigger ||
          !anim.applyInitialState),
      this,
    );

    WidgetsBinding.instance.addPostFrameCallback((_) => setState(() {}));
  }

  @override
  void dispose() {
    _model.dispose();

    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => FocusScope.of(context).requestFocus(_model.unfocusNode),
      child: Scaffold(
        key: scaffoldKey,
        backgroundColor: FlutterFlowTheme.of(context).magnolia,
        appBar: PreferredSize(
          preferredSize: Size.fromHeight(80.0),
          child: AppBar(
            backgroundColor: FlutterFlowTheme.of(context).hunyadiYellow,
            automaticallyImplyLeading: false,
            actions: [],
            flexibleSpace: FlexibleSpaceBar(
              title: Align(
                alignment: AlignmentDirectional(0.00, 0.00),
                child: Text(
                  'Home',
                  style: FlutterFlowTheme.of(context).headlineMedium.override(
                        fontFamily: 'Outfit',
                        color: Colors.white,
                        fontSize: 30.0,
                      ),
                ),
              ),
              centerTitle: true,
              expandedTitleScale: 1.0,
            ),
            bottom: PreferredSize(
              preferredSize: Size.fromHeight(70.0),
              child: Container(),
            ),
            elevation: 2.0,
          ),
        ),
        body: SafeArea(
          top: true,
          child: Row(
            mainAxisSize: MainAxisSize.max,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Column(
                mainAxisSize: MainAxisSize.max,
                children: [
                  Padding(
                    padding:
                        EdgeInsetsDirectional.fromSTEB(0.0, 0.0, 0.0, 20.0),
                    child: Container(
                      width: 272.0,
                      height: 119.0,
                      decoration: BoxDecoration(
                        color: FlutterFlowTheme.of(context).magnolia,
                      ),
                      child: Align(
                        alignment: AlignmentDirectional(0.00, 0.00),
                        child: ClipRRect(
                          borderRadius: BorderRadius.circular(8.0),
                          child: Image.asset(
                            'assets/images/Name.png',
                            width: 440.0,
                            height: 382.0,
                            fit: BoxFit.fitWidth,
                            alignment: Alignment(0.00, 0.00),
                          ),
                        ),
                      ),
                    ),
                  ),
                  Container(
                    width: 133.0,
                    height: 133.0,
                    decoration: BoxDecoration(
                      color: FlutterFlowTheme.of(context).magnolia,
                      shape: BoxShape.circle,
                    ),
                    child: Align(
                      alignment: AlignmentDirectional(0.00, 1.00),
                      child: FlutterFlowIconButton(
                        borderColor:
                            FlutterFlowTheme.of(context).caribbeanCurrent,
                        borderRadius: 150.0,
                        borderWidth: 1.0,
                        buttonSize: 150.0,
                        fillColor: FlutterFlowTheme.of(context).pictonBlue,
                        icon: Icon(
                          Icons.mic_rounded,
                          color: FlutterFlowTheme.of(context).black,
                          size: 100.0,
                        ),
                        onPressed: () async {
                          // Tap Microphone
                          await requestPermission(microphonePermission);
                          if (await getPermissionStatus(microphonePermission)) {
                            // Start Recording
                            _model.audioRecorder ??= Record();
                            if (await _model.audioRecorder!.hasPermission()) {
                              await _model.audioRecorder!.start();
                            } else {
                              showSnackbar(
                                context,
                                'You have not provided permission to record audio.',
                              );
                            }

                            // Dance Microphone
                            if (animationsMap[
                                    'iconButtonOnActionTriggerAnimation'] !=
                                null) {
                              animationsMap[
                                      'iconButtonOnActionTriggerAnimation']!
                                  .controller
                                ..reset()
                                ..repeat();
                            }
                          } else {
                            // Information Dialog
                            await showDialog(
                              context: context,
                              builder: (alertDialogContext) {
                                return AlertDialog(
                                  title: Text('Microphone access'),
                                  content: Text(
                                      'Speedge cannot work if you do not give it access to your device\'s microphone. This is necessary to capture the message you want to translate.'),
                                  actions: [
                                    TextButton(
                                      onPressed: () =>
                                          Navigator.pop(alertDialogContext),
                                      child: Text('Ok'),
                                    ),
                                  ],
                                );
                              },
                            );
                          }
                        },
                      ).animateOnActionTrigger(
                        animationsMap['iconButtonOnActionTriggerAnimation']!,
                      ),
                    ),
                  ),
                  Padding(
                    padding:
                        EdgeInsetsDirectional.fromSTEB(0.0, 0.0, 0.0, 60.0),
                    child: Container(
                      width: 173.0,
                      height: 100.0,
                      decoration: BoxDecoration(
                        color: FlutterFlowTheme.of(context).magnolia,
                      ),
                      child: Align(
                        alignment: AlignmentDirectional(0.00, -1.00),
                        child: Text(
                          'Start recording',
                          style:
                              FlutterFlowTheme.of(context).bodyMedium.override(
                                    fontFamily: 'Readex Pro',
                                    color: FlutterFlowTheme.of(context).black,
                                    fontSize: 22.0,
                                    fontWeight: FontWeight.normal,
                                  ),
                        ),
                      ),
                    ),
                  ),
                  Container(
                    width: 100.0,
                    height: 100.0,
                    decoration: BoxDecoration(
                      color: FlutterFlowTheme.of(context).magnolia,
                    ),
                    child: Align(
                      alignment: AlignmentDirectional(0.00, 0.00),
                      child: FlutterFlowIconButton(
                        borderColor: FlutterFlowTheme.of(context).black,
                        borderRadius: 0.0,
                        borderWidth: 1.0,
                        buttonSize: 100.0,
                        fillColor: FlutterFlowTheme.of(context).persianRed,
                        icon: Icon(
                          Icons.stop_circle,
                          color: FlutterFlowTheme.of(context).magnolia,
                          size: 80.0,
                        ),
                        onPressed: () async {
                          // StopRecording
                          _model.inputAudio =
                              await _model.audioRecorder?.stop();
                          // StopRecorrdingButtonDance
                          if (animationsMap[
                                  'iconButtonOnActionTriggerAnimation'] !=
                              null) {
                            animationsMap['iconButtonOnActionTriggerAnimation']!
                                .controller
                                .stop();
                          }
                          await PassBinaryCall.call();

                          context.pushNamed(
                            'Processing',
                            queryParameters: {
                              'inputAudio': serializeParam(
                                _model.inputAudio,
                                ParamType.String,
                              ),
                              'userName': serializeParam(
                                widget.userName,
                                ParamType.String,
                              ),
                            }.withoutNulls,
                          );

                          setState(() {});
                        },
                      ),
                    ),
                  ),
                  Container(
                    width: 165.0,
                    height: 100.0,
                    decoration: BoxDecoration(
                      color: FlutterFlowTheme.of(context).magnolia,
                    ),
                    child: Align(
                      alignment: AlignmentDirectional(0.00, -1.00),
                      child: Text(
                        'Stop recording',
                        style: FlutterFlowTheme.of(context).bodyMedium.override(
                              fontFamily: 'Readex Pro',
                              color: FlutterFlowTheme.of(context).black,
                              fontSize: 22.0,
                              fontWeight: FontWeight.normal,
                            ),
                      ),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
