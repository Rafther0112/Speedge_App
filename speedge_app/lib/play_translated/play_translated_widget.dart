import '/flutter_flow/flutter_flow_audio_player.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/flutter_flow/flutter_flow_widgets.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';
import 'play_translated_model.dart';
export 'play_translated_model.dart';

class PlayTranslatedWidget extends StatefulWidget {
  const PlayTranslatedWidget({
    Key? key,
    required this.inputAudio,
    required this.userName,
  }) : super(key: key);

  final String? inputAudio;
  final String? userName;

  @override
  _PlayTranslatedWidgetState createState() => _PlayTranslatedWidgetState();
}

class _PlayTranslatedWidgetState extends State<PlayTranslatedWidget> {
  late PlayTranslatedModel _model;

  final scaffoldKey = GlobalKey<ScaffoldState>();

  @override
  void initState() {
    super.initState();
    _model = createModel(context, () => PlayTranslatedModel());

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
            title: Align(
              alignment: AlignmentDirectional(0.00, 0.00),
              child: Text(
                'Your message has been translated :)',
                textAlign: TextAlign.center,
                maxLines: 2,
                style: FlutterFlowTheme.of(context).headlineMedium.override(
                      fontFamily: 'Outfit',
                      color: Colors.white,
                      fontSize: 30.0,
                      lineHeight: 1.0,
                    ),
              ),
            ),
            actions: [],
            centerTitle: false,
            elevation: 2.0,
          ),
        ),
        body: SafeArea(
          top: true,
          child: Padding(
            padding: EdgeInsetsDirectional.fromSTEB(10.0, 0.0, 10.0, 0.0),
            child: Row(
              mainAxisSize: MainAxisSize.max,
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Column(
                  mainAxisSize: MainAxisSize.max,
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Container(
                      width: 368.0,
                      height: 100.0,
                      decoration: BoxDecoration(
                        color: FlutterFlowTheme.of(context).magnolia,
                      ),
                      child: Padding(
                        padding:
                            EdgeInsetsDirectional.fromSTEB(5.0, 5.0, 5.0, 5.0),
                        child: FlutterFlowAudioPlayer(
                          audio: Audio.network(
                            widget.inputAudio!,
                            metas: Metas(
                              id: '2vqf7_-4e415a0d',
                              title: 'Tap to play translated audio',
                            ),
                          ),
                          titleTextStyle:
                              FlutterFlowTheme.of(context).titleLarge,
                          playbackDurationTextStyle:
                              FlutterFlowTheme.of(context).labelMedium,
                          fillColor:
                              FlutterFlowTheme.of(context).secondaryBackground,
                          playbackButtonColor:
                              FlutterFlowTheme.of(context).caribbeanCurrent,
                          activeTrackColor:
                              FlutterFlowTheme.of(context).alternate,
                          elevation: 4.0,
                          playInBackground:
                              PlayInBackground.disabledRestoreOnForeground,
                        ),
                      ),
                    ),
                    Padding(
                      padding:
                          EdgeInsetsDirectional.fromSTEB(0.0, 100.0, 0.0, 0.0),
                      child: FFButtonWidget(
                        onPressed: () async {
                          context.pushNamed('Home');
                        },
                        text: 'Record again',
                        options: FFButtonOptions(
                          height: 40.0,
                          padding: EdgeInsetsDirectional.fromSTEB(
                              24.0, 0.0, 24.0, 0.0),
                          iconPadding: EdgeInsetsDirectional.fromSTEB(
                              0.0, 0.0, 0.0, 0.0),
                          color: FlutterFlowTheme.of(context).caribbeanCurrent,
                          textStyle:
                              FlutterFlowTheme.of(context).titleSmall.override(
                                    fontFamily: 'Readex Pro',
                                    color: Colors.white,
                                  ),
                          elevation: 3.0,
                          borderSide: BorderSide(
                            color: Colors.transparent,
                            width: 1.0,
                          ),
                          borderRadius: BorderRadius.circular(8.0),
                        ),
                      ),
                    ),
                    Padding(
                      padding:
                          EdgeInsetsDirectional.fromSTEB(0.0, 100.0, 0.0, 0.0),
                      child: Container(
                        width: 290.0,
                        height: 100.0,
                        decoration: BoxDecoration(
                          color: FlutterFlowTheme.of(context).magnolia,
                        ),
                        child: ClipRRect(
                          borderRadius: BorderRadius.circular(8.0),
                          child: Image.asset(
                            'assets/images/Name.png',
                            width: 300.0,
                            height: 200.0,
                            fit: BoxFit.fitWidth,
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
      ),
    );
  }
}
